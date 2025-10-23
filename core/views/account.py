from rest_framework import viewsets
from ..models.account import User, StudentProfile, BoothManagerProfile
from ..serializers.account import UserSerializer, StudentProfileSerializer, BoothManagerProfileSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class StudentProfileViewSet(viewsets.ModelViewSet):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer

class BoothManagerProfileViewSet(viewsets.ModelViewSet):
    queryset = BoothManagerProfile.objects.all()
    serializer_class = BoothManagerProfileSerializer
