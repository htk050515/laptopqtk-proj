from rest_framework import serializers
from .models import Laptop, Accessory, Order, OrderItem
from django.db import transaction

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

class CreateOrderItemSerializer(serializers.Serializer):
    product_type = serializers.ChoiceField(choices=OrderItem.PRODUCT_TYPE_CHOICES)
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField()

class CreateOrderSerializer(serializers.Serializer):
    items = CreateOrderItemSerializer(many=True)

    def create(self, validated_data):
        user = self.context['request'].user
        items_data = validated_data['items']

        with transaction.atomic():
            order = Order.objects.create(user=user)

            total_price = 0

            for item in items_data:
                product_type = item['product_type']
                product_id = item['product_id']
                quantity = item['quantity']

                if product_type == 'LAPTOP':
                    product = Laptop.objects.get(id=product_id)
                else:
                    product = Accessory.objects.get(id=product_id)

                if product.stock < quantity:
                    raise serializers.ValidationError("Not enough stock")

                product.stock -= quantity
                product.save()

                subtotal = product.price * quantity
                total_price += subtotal

                OrderItem.objects.create(
                    order=order,
                    product_type=product_type,
                    product_id=product.id,
                    product_name=product.name,
                    price=product.price,
                    quantity=quantity
                )

            order.total_price = total_price
            order.save()

        return order
