from rest_framework.routers import DefaultRouter
from django.urls import path

from .views import PublicationViewset

router = DefaultRouter()
router.register(r'', PublicationViewset)
urlpatterns = router.urls
