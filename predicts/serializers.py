from django.db import models
from .models import Predict,WhoScoreFirst,MatchPredict
from rest_framework import serializers


class PredictSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchPredict
        fields = '__all__'
        
    
    
class CreatePredictSerializer(serializers.ModelSerializer):
    match_id = serializers.IntegerField()
    class Meta : 
        model = Predict
        fields = ('match_id','resultA','resultB','who_score_first','name','email','phone')

    
    