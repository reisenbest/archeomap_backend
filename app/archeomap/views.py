from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import status, viewsets
from .serializers import *
from .models.models import *

class TestModelViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = TestModel.objects.all()
    serializer_class = TestModelSerializer

class CategoryModelViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = TestCategory.objects.all()
    serializer_class = TestCategorySerializer

#TODO: переопределить метод post , сейчас нельзя заполнить поля которые ManytoMany
class MonumentsModelViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    """
    queryset = Monuments.objects.all()
    serializer_class = MonumentsSerializer

class ImagesListAPIView(generics.ListAPIView):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer


