from rest_framework import viewsets, generics, permissions
from .models import Laptop, Accessory, Order
from .serializers import LaptopSerializer, AccessorySerializer, OrderSerializer, CreateOrderSerializer
from .permissions import IsAdminOrStaff

class LaptopViewSet(viewsets.ModelViewSet):
    queryset = Laptop.objects.filter(is_active=True)
    serializer_class = LaptopSerializer
    permission_classes = [IsAdminOrStaff]
    lookup_field = 'slug'

class AccessoryViewSet(viewsets.ModelViewSet):
    queryset = Accessory.objects.filter(is_active=True)
    serializer_class = AccessorySerializer
    permission_classes = [IsAdminOrStaff]
    lookup_field = 'slug'

class CreateOrderView(generics.CreateAPIView):
    serializer_class = CreateOrderSerializer
    permission_classes = [permissions.IsAuthenticated]

class OrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role in ['ADMIN', 'STAFF']:
            return Order.objects.all()
        return Order.objects.filter(user=user)

class OrderDetailView(generics.RetrieveAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Order.objects.all()
