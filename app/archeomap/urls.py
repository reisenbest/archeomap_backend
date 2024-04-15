from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import TestModelViewSet, CategoryModelViewSet, MonumentsModelViewSet


router_city = SimpleRouter()
router_city.register(r'testmodel', TestModelViewSet)

router_category = SimpleRouter()
router_category.register(r'cat', CategoryModelViewSet)

router_monuments = SimpleRouter()
router_monuments.register(r'monuments', MonumentsModelViewSet)


urlpatterns = [
    path ('', include(router_city.urls)),
    path ('', include(router_category.urls)),
    path ('', include(router_monuments.urls))

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)