from rest_framework.routers import DefaultRouter

from apps.comments.views import Comment

router = DefaultRouter()
router.register(r'comments', Comment)
urlpatterns = router.urls
