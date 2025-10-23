from rest_framework import viewsets
from ..models.booth import Booth, BoothEvent, Rating, ContestSetting, ContestWinner
from ..serializers.booth import BoothSerializer, BoothEventSerializer, RatingSerializer, ContestSettingSerializer, ContestWinnerSerializer

class BoothViewSet(viewsets.ModelViewSet):
    queryset = Booth.objects.all()
    serializer_class = BoothSerializer

class BoothEventViewSet(viewsets.ModelViewSet):
    queryset = BoothEvent.objects.all()
    serializer_class = BoothEventSerializer

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

class ContestSettingViewSet(viewsets.ModelViewSet):
    queryset = ContestSetting.objects.all()
    serializer_class = ContestSettingSerializer

class ContestWinnerViewSet(viewsets.ModelViewSet):
    queryset = ContestWinner.objects.all()
    serializer_class = ContestWinnerSerializer
