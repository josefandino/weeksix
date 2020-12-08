from rest_framework.routers import DefaultRouter

from .views import Tagviewsets

router = DefaultRouter()

router.register(r'', Tagviewsets)

urlpatterns = router.urls
