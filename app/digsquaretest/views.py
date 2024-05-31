from rest_framework import generics
from .models import MonumentTest
from .serializers import MonumentTestSerializer

class MonumentTestListView(generics.ListAPIView):
    queryset = MonumentTest.objects.all()
    serializer_class = MonumentTestSerializer