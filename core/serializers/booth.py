from rest_framework import serializers
from ..models.booth import Booth, BoothEvent, Rating, ContestSetting, ContestWinner

class BoothSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booth
        fields = '__all__'

class BoothEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoothEvent
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'

class ContestSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContestSetting
        fields = '__all__'

class ContestWinnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContestWinner
        fields = '__all__'
