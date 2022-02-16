from rest_framework.routers import DefaultRouter
from resizer.views import ImagesDetailViewSet

router = DefaultRouter()
router.register(r'images', ImagesDetailViewSet, basename='resizer')
urlpatterns = router.urls
