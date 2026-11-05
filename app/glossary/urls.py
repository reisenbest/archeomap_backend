from django.urls import path

from .views import (
    GlossaryTermDetailAPIView,
    GlossaryTermListAPIView,
)


app_name = "glossary"

urlpatterns = [
    path(
        "glossary/",
        GlossaryTermListAPIView.as_view(),
        name="term-list",
    ),
    path(
        "glossary/<int:pk>/",
        GlossaryTermDetailAPIView.as_view(),
        name="term-detail",
    ),
]