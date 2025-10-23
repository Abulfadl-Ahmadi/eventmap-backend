from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
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


# نمایش اطلاعات کاربر جاری
class CurrentUserAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
