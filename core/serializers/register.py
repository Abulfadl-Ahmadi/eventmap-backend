from rest_framework import serializers
from core.models.account import User, StudentProfile
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    student_code = serializers.CharField(required=False, allow_blank=True)
    faculty = serializers.CharField(required=False, allow_blank=True)
    entrance_year = serializers.IntegerField(required=False, allow_null=True)

    class Meta:
        model = User
        fields = (
            'username', 'password', 'password2', 'email', 'first_name', 'last_name', 'role',
            'phone_number', 'national_id', 'student_code', 'faculty', 'entrance_year'
        )

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        student_code = validated_data.pop('student_code', None)
        faculty = validated_data.pop('faculty', None)
        entrance_year = validated_data.pop('entrance_year', None)
        user = User.objects.create_user(**validated_data)
        if user.role == User.Roles.STUDENT:
            StudentProfile.objects.create(
                user=user,
                student_code=student_code or '',
                faculty=faculty or '',
                entrance_year=entrance_year
            )
        return user
