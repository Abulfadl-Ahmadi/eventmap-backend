from rest_framework import serializers
from ..models.account import User, StudentProfile, BoothManagerProfile


class UserSerializer(serializers.ModelSerializer):
    # Optional profile fields for student
    student_code = serializers.CharField(required=False, allow_blank=True)
    faculty = serializers.CharField(required=False, allow_blank=True)
    entrance_year = serializers.IntegerField(required=False, allow_null=True)

    class Meta:
        model = User
        fields = [
            'id', 'username', 'first_name', 'last_name', 'email', 'role',
            'phone_number', 'national_id', 'is_active', 'is_staff', 'is_superuser',
            'student_code', 'faculty', 'entrance_year',
        ]

    def create(self, validated_data):
        student_code = validated_data.pop('student_code', None)
        faculty = validated_data.pop('faculty', None)
        entrance_year = validated_data.pop('entrance_year', None)
        user = super().create(validated_data)
        if user.role == User.Roles.STUDENT:
            StudentProfile.objects.update_or_create(
                user=user,
                defaults={
                    'student_code': student_code or '',
                    'faculty': faculty or '',
                    'entrance_year': entrance_year,
                }
            )
        return user

class StudentProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = StudentProfile
        fields = ['id', 'user', 'student_code', 'faculty', 'entrance_year']

class BoothManagerProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = BoothManagerProfile
        fields = ['id', 'user']
