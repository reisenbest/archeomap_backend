from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny



from .models import Articles
from .serializers import (
    ArticlesListSerializer,
    ArticlesDetailSerializer,
)


# Create your views here.

class ArticlesListAPIView(generics.ListAPIView):
    serializer_class = ArticlesListSerializer
    permission_classes = (AllowAny,)

    queryset = (
        Articles.objects
        .filter(is_published=True)
        .select_related('preview_image')
        .prefetch_related('categories', 'tags', 'authors')
        .order_by('-created_at', '-id')
    )


class ArticlesDetailAPIView(generics.RetrieveAPIView):
    serializer_class = ArticlesDetailSerializer
    permission_classes = (AllowAny,)
    lookup_field = 'slug'

    queryset = (
        Articles.objects
        .filter(is_published=True)
        .select_related('preview_image')
        .prefetch_related(
            'categories',
            'tags',
            'authors',
            'images',
        )
    )

