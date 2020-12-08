from rest_framework.routers import DefaultRouter
from django.urls import path

from .views import PublicacionViewSet

router = DefaultRouter()
router.register(r'', PublicacionViewSet)
urlpatterns = router.urls
