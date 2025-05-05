from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *




urlpatterns = [
    path('monuments/', MonumentsPublicListAPIView.as_view(), name='monuments-list'),
    path('monuments/<int:monument_id>/', MonumentPublicDetailAPIView.as_view(), name='monument-detail'),
    path('monuments/classificationlist/', ClassificationListAPIView.as_view(), name='classification-list'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)