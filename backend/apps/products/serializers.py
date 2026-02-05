from rest_framework import serializers
from .models import Laptop, Accessory, Order, OrderItem

class LaptopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laptop
        fields = [
            'id',
            'name',
            'brand',
            'price',
            'stock',
            'cpu',
            'ram',
            'storage',
            'gpu',
            'screen',
            'description',
            'image',
            'slug',
            'is_active',
            'created_at',
        ]

class AccessorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Accessory
        fields = [
            'id',
            'name',
            'category',
            'price',
            'stock',
            'description',
            'image',
            'slug',
            'is_active',
            'created_at',
        ]

class OrderItemSerializer(serializers.ModelSerializer):
    subtotal = serializers.SerializerMethodField()

    class Meta:
        model = OrderItem
        fields = [
            'id',
            'product_type',
            'product_id',
            'product_name',
            'price',
            'quantity',
            'subtotal',
        ]

    def get_subtotal(self, obj):
        return obj.price * obj.quantity

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    user_email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = Order
        fields = [
            'id',
            'user_email',
            'total_price',
            'status',
            'created_at',
            'items',
        ]
