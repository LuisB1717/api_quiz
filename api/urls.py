from rest_framework import routers

from .api import CategoryViewSet, QuestionViewSet

router = routers.DefaultRouter()

router.register('api/questions', QuestionViewSet, 'questions')
router.register('api/categories', CategoryViewSet, 'categories')

urlpatterns = router.urls
