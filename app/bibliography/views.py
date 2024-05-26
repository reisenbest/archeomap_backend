from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import status, viewsets
from .serializers import BibliographyOutputSerializer
from .models.models import Bibliography
from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from bibliography.docs import *
from app.settings import BASE_DIR


#TODO: тесты 
class BibliographyListAPIView(APIView):
    output_serializer = BibliographyOutputSerializer

    # @get_monuments__public_scheme
    def get(self, request):
        bibliography_list =  Bibliography.objects.all()
        data = self.output_serializer(bibliography_list, many=True).data
        return Response(data, status=status.HTTP_200_OK)



# class BibliographyDetailAPIView(APIView):
#     output_serializer = BibliographyOutputSerializer

#     def get(self, request, bibliography_id):
#         try:
#             bibliography_object = Bibliography.objects.get(id=bibliography_id)
#         except Bibliography.DoesNotExist:
#             return Response(
#                 {"error": "Bibliography-object does not exist"},
#                 status=status.HTTP_404_NOT_FOUND
#             )

#         data = self.output_serializer(bibliography_object).data
#         return Response(data, status=status.HTTP_200_OK)