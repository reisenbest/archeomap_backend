from rest_framework import serializers

from .models import GlossaryTerm


class GlossaryTermSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlossaryTerm
        fields = (
            "id",
            "title",
            "slug",
            "short_definition",
        )
        read_only_fields = fields

