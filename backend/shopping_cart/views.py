from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Order, OrderItem, Cart, CartItem
from users.models import User, Address
from product.models import Product
from .serializers import OrderSerializer, OrderItemSerializer, CartSerializer, CartItemSerializer

# Create your views here.

# OrderView
class OrderView(APIView):

    def get(self, request, pk=None):
        if pk:
            try:
                order = Order.objects.get(pk=pk)
            except Order.DoesNotExist:
                return Response({"detail": "Order not found."}, status=404)
            serializer = OrderSerializer(order)
            return Response(serializer.data)
        else:
            orders = Order.objects.all()
            serializer = OrderSerializer(orders, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def patch(self, request, pk):
        try:
            order = Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            return Response({"detail": "Order not found."}, status=404)
        serializer = OrderSerializer(order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        try:
            order = Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            return Response({"detail": "Order not found."}, status=404)
        order.delete()
        return Response(status=204)

# OrderItemView
class OrderItemView(APIView):

    def get(self, request, pk=None):
        if pk:
            try:
                order_item = OrderItem.objects.get(pk=pk)
            except OrderItem.DoesNotExist:
                return Response({"detail": "Order item not found."}, status=404)
            serializer = OrderItemSerializer(order_item)
            return Response(serializer.data)
        else:
            order_items = OrderItem.objects.all()
            serializer = OrderItemSerializer(order_items, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = OrderItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def patch(self, request, pk):
        try:
            order_item = OrderItem.objects.get(pk=pk)
        except OrderItem.DoesNotExist:
            return Response({"detail": "Order item not found."}, status=404)
        serializer = OrderItemSerializer(order_item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        try:
            order_item = OrderItem.objects.get(pk=pk)
        except OrderItem.DoesNotExist:
            return Response({"detail": "Order item not found."}, status=404)
        order_item.delete()
        return Response(status=204)

# CartView
class CartView(APIView):

    def get(self, request, pk=None):
        if pk:
            try:
                cart = Cart.objects.get(pk=pk)
            except Cart.DoesNotExist:
                return Response({"detail": "Cart not found."}, status=404)
            serializer = CartSerializer(cart)
            return Response(serializer.data)
        else:
            # Allow filtering carts by user if requested
            user = request.query_params.get('user')
            if user:
                try:
                    user = User.objects.get(pk=user)
                except User.DoesNotExist:
                    return Response({"detail": "Invalid user."}, status=400)
                carts = Cart.objects.filter(user=user)
            else:
                carts = Cart.objects.all()
            serializer = CartSerializer(carts, many=True)
            return Response(serializer.data)

    def post(self, request):
        # Assume user information is provided in request data
        user = request.data.get('user')
        if not user:
            return Response({"detail": "User information required."}, status=400)
        try:
            user = User.objects.get(pk=user)
        except User.DoesNotExist:
            return Response({"detail": "Invalid user."}, status=400)
        # Check if user already has a cart
        if Cart.objects.filter(user=user).exists():
            return Response({"detail": "User already has a cart."}, status=400)
        serializer = CartSerializer(data={'user': user})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def patch(self, request, pk):
        try:
            cart = Cart.objects.get(pk=pk)
        except Cart.DoesNotExist:
            return Response({"detail": "Cart not found."}, status=404)
        # Allow updating user if provided
        user = request.data.get('user')
        if user:
            try:
                user = User.objects.get(pk=user)
            except User.DoesNotExist:
                return Response({"detail": "Invalid user."}, status=400)
            cart.user = user
            cart.save()
        # Other cart fields can also be updated here based on your needs
        # ...
        serializer = CartSerializer(cart, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        try:
            cart = Cart.objects.get(pk=pk)
        except Cart.DoesNotExist:
            return Response({"detail": "Cart not found."}, status=404)
        cart.delete()
        return Response(status=204)

# CartItemView
class CartItemView(APIView):

    def get(self, request, pk=None):
        if pk:
            try:
                cart_item = CartItem.objects.get(pk=pk)
            except CartItem.DoesNotExist:
                return Response({"detail": "Cart item not found."}, status=404)
            serializer = CartItemSerializer(cart_item)
            return Response(serializer.data)
        else:
            # Allow filtering by cart and product
            cart = request.query_params.get('cart')
            product = request.query_params.get('product')
            if cart:
                try:
                    cart = Cart.objects.get(pk=cart)
                except Cart.DoesNotExist:
                    return Response({"detail": "Invalid cart."}, status=400)
                cart_items = CartItem.objects.filter(cart=cart)
            if product:
                try:
                    product = Product.objects.get(pk=product)
                except Product.DoesNotExist:
                    return Response({"detail": "Invalid product."}, status=400)
                if cart:
                    cart_items = cart_items.filter(product=product)
                else:
                    cart_items = CartItem.objects.filter(product=product)
            else:
                if cart:
                    cart_items = CartItem.objects.filter(cart=cart)
                else:
                    cart_items = CartItem.objects.all()
            serializer = CartItemSerializer(cart_items, many=True)
            return Response(serializer.data)

    def post(self, request):
        # Assume cart and product information are provided
        cart = request.data.get('cart')
        product = request.data.get('product')
        quantity = request.data.get('quantity', 1)
        if not cart or not product:
            return Response({"detail": "Cart and product information required."}, status=400)
        try:
            cart = Cart.objects.get(pk=cart)
        except Cart.DoesNotExist:
            return Response({"detail": "Invalid cart."}, status=400)
        try:
            product = Product.objects.get(pk=product)
        except Product.DoesNotExist:
            return Response({"detail": "Invalid product."}, status=400)
        # Check if item already exists in cart
        if CartItem.objects.filter(cart=cart, product=product).exists():
            return Response({"detail": "Item already exists in cart."}, status=400)
        serializer = CartItemSerializer(data={'cart': cart, 'product': product, 'quantity': quantity})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def patch(self, request, pk):
        try:
            cart_item = CartItem.objects.get(pk=pk)
        except CartItem.DoesNotExist:
            return Response({"detail": "Cart item not found."}, status=404)
        # Allow updating cart, product, or quantity if provided
        cart = request.data.get('cart')
        product = request.data.get('product')
        quantity = request.data.get('quantity')
        if cart:
            try:
                cart = Cart.objects.get(pk=cart)
            except Cart.DoesNotExist:
                return Response({"detail": "Invalid cart."}, status=400)
            cart_item.cart = cart
        if product:
            try:
                product = Product.objects.get(pk=product)
            except Product.DoesNotExist:
                return Response({"detail": "Invalid product."}, status=400)
            cart_item.product = product
        if quantity:
            cart_item.quantity = quantity
        cart_item.save()
        serializer = CartItemSerializer(cart_item)
        return Response(serializer.data)

    def delete(self, request, pk):
        try:
            cart_item = CartItem.objects.get(pk=pk)
        except CartItem.DoesNotExist:
            return Response({"detail": "Cart item not found."}, status=404)
        cart_item.delete()
        return Response(status=204)
