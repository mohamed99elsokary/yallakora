from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import serializers, models


@api_view(["GET"])
def images(request):
    images = models.Image.objects.all()
    serializer = serializers.ImageSerializer(images, many=True)
    return Response(serializer.data)
