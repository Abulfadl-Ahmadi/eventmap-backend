from rest_framework import serializers
from ..models.content import BoothResource, PhotoSubmission, PhotoSubmissionAudit

class BoothResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoothResource
        fields = '__all__'

class PhotoSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoSubmission
        fields = '__all__'

class PhotoSubmissionAuditSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoSubmissionAudit
        fields = '__all__'
