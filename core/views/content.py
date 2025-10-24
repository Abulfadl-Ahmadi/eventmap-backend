from rest_framework import viewsets
from ..models.content import BoothResource, PhotoSubmission, PhotoSubmissionAudit
from ..serializers.content import BoothResourceSerializer, PhotoSubmissionSerializer, PhotoSubmissionAuditSerializer

class BoothResourceViewSet(viewsets.ModelViewSet):
    queryset = BoothResource.objects.all()
    serializer_class = BoothResourceSerializer

class PhotoSubmissionViewSet(viewsets.ModelViewSet):
    queryset = PhotoSubmission.objects.all()
    serializer_class = PhotoSubmissionSerializer

class PhotoSubmissionAuditViewSet(viewsets.ModelViewSet):
    queryset = PhotoSubmissionAudit.objects.all()
    serializer_class = PhotoSubmissionAuditSerializer
