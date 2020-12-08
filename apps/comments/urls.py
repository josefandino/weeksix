from rest_framework.routers import DefaultRouter

from apps.comments.views import CommentView

router = DefaultRouter()
router.register(r'comments', CommentView)
urlpatterns = router.urls
