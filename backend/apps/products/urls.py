from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import (
    LaptopViewSet,
    AccessoryViewSet,
    CreateOrderView,
    OrderListView,
    OrderDetailView
)

# Router cho ViewSet
router = DefaultRouter()
router.register(r'laptops', LaptopViewSet, basename='laptop')
router.register(r'accessories', AccessoryViewSet, basename='accessory')

# Kết hợp router và custom views
urlpatterns = [
    path('', include(router.urls)),
    
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('orders/create/', CreateOrderView.as_view(), name='order-create'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
]
