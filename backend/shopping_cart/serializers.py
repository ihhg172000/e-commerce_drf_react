from rest_framework import serializers
from users.serializers import UserSerializer, AddressSerializer
from product.serializers import ProductSerializer
from .models import Order, OrderItem, Cart, CartItem

# serialization goes here

class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    address = AddressSerializer()
    items = ProductSerializer(many=True)
    class Meta:
        model = Order
        fields = ('id', 'user', 'address', 'items', 'paid', 'delivered', 'created_at', 'updated_at')

class OrderItemSerializer(serializers.ModelSerializer):
    order = OrderSerializer()
    product = ProductSerializer()
    class Meta:
        model = OrderItem
        fields = ('id', 'order', 'product', 'quantity', 'created_at', 'updated_at')

class CartSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    items = ProductSerializer(many=True)
    class Meta:
        model = Cart
        fields = ('id', 'user', 'items', 'created_at', 'updated_at')

class CartItemSerializer(serializers.ModelSerializer):
    cart = CartSerializer()
    product = ProductSerializer()
    class Meta:
        model = CartItem
        fields = ('id', 'cart', 'product', 'created_at', 'updated_at')
