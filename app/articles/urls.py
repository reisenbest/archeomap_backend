from django.urls import path

from .views import ArticlesListAPIView, ArticlesDetailAPIView


app_name = 'articles'

urlpatterns = [
    path(
        'articles/',
        ArticlesListAPIView.as_view(),
        name='article-list',
    ),
    path(
        'articles/<slug:slug>/',
        ArticlesDetailAPIView.as_view(),
        name='article-detail',
    ),
]