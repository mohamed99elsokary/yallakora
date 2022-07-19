from django.shortcuts import render
from .models import Social
from .serializers import SocialSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class getSocial(APIView):
    def get(self, request):
        social = Social.objects.first()
        serializer = SocialSerializer(social, context={'request': request})
        return Response(serializer.data)