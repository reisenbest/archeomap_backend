from rest_framework import serializers
from bibliography.models.models import Bibliography

class BibliographyOutputSerializer(serializers.ModelSerializer):

  class Meta:
    model = Bibliography
    fields = '__all__'