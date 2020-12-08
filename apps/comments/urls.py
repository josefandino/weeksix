from rest_framework.routers import DefaultRouter

<<<<<<< HEAD
from apps.comments.views import CommentView

router = DefaultRouter()
router.register(r'comments', CommentView)
=======
from ..comments.views import CommentView

router = DefaultRouter()
router.register(r'', CommentView)
>>>>>>> 13ddd2046f9259766f16ab407bf620a236704a09
urlpatterns = router.urls
