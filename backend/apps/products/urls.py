from rest_framework.routers import DefaultRouter
from .views import LaptopViewSet, AccessoryViewSet

router = DefaultRouter()
router.register(r'laptops', LaptopViewSet, basename='laptop')
router.register(r'accessories', AccessoryViewSet, basename='accessory')


urlpatterns = router.urls
