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
from app.settings import BASE_DIR


#TODO: тесты + вынести запрос в queries + добавить пагинацию?
class MonumentsPublicListAPIView(APIView):
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
                                                        'excavations_square',
                                                        ).all()
        data = self.output_serializer(monuments, many=True).data
        print(BASE_DIR)
        return Response(data, status=status.HTTP_200_OK)



class MonumentPublicDetailAPIView(APIView):
    output_serializer = MonumentsPublicOutputSerializer

    def get(self, request, monument_id):
        try:
            monument = Monuments.objects.prefetch_related(
                'dating',
                'classification_category',
                'custom_category',
                'research_years',
                'authors',
                'organizations',
                'sources',
                'content',
                'images',
                'excavations_square',
            ).get(id=monument_id)
        except Monuments.DoesNotExist:
            return Response(
                {"error": "Monument does not exist"},
                status=status.HTTP_404_NOT_FOUND
            )

        data = self.output_serializer(monument).data
        return Response(data, status=status.HTTP_200_OK)