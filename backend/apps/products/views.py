from rest_framework import viewsets
from .models import Laptop, Accessory
from .serializers import LaptopSerializer, AccessorySerializer
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