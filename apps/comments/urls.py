from rest_framework.routers import DefaultRouter

from ..comments.views import CommentView

router = DefaultRouter()
router.register(r'', CommentView)
urlpatterns = router.urls
