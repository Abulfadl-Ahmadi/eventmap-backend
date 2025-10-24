from rest_framework import viewsets
from rest_framework.response import Response
from ..models.booth import Booth, BoothEvent, Rating, ContestSetting, ContestWinner
from ..serializers.booth import BoothSerializer, BoothEventSerializer, RatingSerializer, ContestSettingSerializer, ContestWinnerSerializer

class BoothViewSet(viewsets.ModelViewSet):
    queryset = Booth.objects.all()
    serializer_class = BoothSerializer

class BoothEventViewSet(viewsets.ModelViewSet):
    queryset = BoothEvent.objects.all()
    serializer_class = BoothEventSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        booth_pk = self.kwargs.get('booth_pk')
        if booth_pk:
            queryset = queryset.filter(booth_id=booth_pk)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'events': serializer.data,
            'upcomingEvents': None,
            'pastEvents': None,
        })

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

class ContestSettingViewSet(viewsets.ModelViewSet):
    queryset = ContestSetting.objects.all()
    serializer_class = ContestSettingSerializer

class ContestWinnerViewSet(viewsets.ModelViewSet):
    queryset = ContestWinner.objects.all()
    serializer_class = ContestWinnerSerializer
