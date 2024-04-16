from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import status, viewsets
from .serializers import *
from .models.models import *
from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from archeomap.docs import *


#TODO: тесты + вынести запрос в queries + добавить пагинацию?
class MonumentsPublicAPIView(APIView):
    output_serializer = MonumentsPublicOutputSerializer

    @get_monuments__public_scheme
    def get(self, request):
        monuments =  Monuments.objects.prefetch_related('dating',
                                                        'classification_category',
                                                        'custom_category',
                                                        'research_years',
                                                        'authors',
                                                        'organizations',
                                                        'sources',
                                                        'content',
                                                        'images',
                                                        ).all()
        data = self.output_serializer(monuments, many=True).data
        print(self.allowed_methods)
        return Response(data, status=status.HTTP_200_OK)


