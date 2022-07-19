from django.shortcuts import render
from .models import Predict,MatchPredict
from .serializers import PredictSerializer,CreatePredictSerializer
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from datetime import datetime
from django.utils import timezone
from rest_framework import status

class getPredicts(APIView):
    def get(self, request):
        predicts = MatchPredict.objects.order_by('-created')
        serializer = PredictSerializer(predicts, many=True, context={'request': request})
        return Response(serializer.data)
    
    
    
class AddPredict(GenericAPIView):
    serializer_class = CreatePredictSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try:
                match = MatchPredict.objects.get(id=serializer.validated_data['match_id'])
            except MatchPredict.DoesNotExist:
                res = {
                    'error' : True,
                    'message' : 'Match does not exist'
                }
                return Response(res, status=400)
            if match.start_date < timezone.now():
                res = {
                    'error':True,
                    'message':'Match has already started'
                    
                }
                return Response(res, status=400)
            email = serializer.validated_data['email']
            predict =  Predict.objects.filter(email=email, match_id=serializer.validated_data['match_id'])
            if predict.exists():
                predict.update(**serializer.validated_data)
                return Response({'message':'Predict updated'}, status=200)
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)