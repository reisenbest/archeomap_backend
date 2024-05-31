from rest_framework import serializers
from .models import MonumentTest

class MonumentTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonumentTest
        fields = ['id', 'title', 'excavation_area']