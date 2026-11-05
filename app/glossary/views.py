from rest_framework import filters, generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny

from .models import GlossaryTerm
from .serializers import GlossaryTermSerializer


class GlossaryPagination(PageNumberPagination):
    page_size = 20


class GlossaryTermListAPIView(generics.ListAPIView):
    serializer_class = GlossaryTermSerializer
    permission_classes = [AllowAny]
    pagination_class = GlossaryPagination

    queryset = GlossaryTerm.objects.filter(
        is_published=True,
    ).order_by("title", "id")

    filter_backends = [filters.SearchFilter]
    search_fields = ["title"]


class GlossaryTermDetailAPIView(generics.RetrieveAPIView):
    serializer_class = GlossaryTermSerializer
    permission_classes = [AllowAny]

    queryset = GlossaryTerm.objects.filter(
        is_published=True,
    )