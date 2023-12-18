from django.urls import path
from .views import OrderView, OrderItemView, CartView, CartItemView

app_name = 'cart'

urlpatterns = [
    path('orders/', OrderView.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderView.as_view(), name='order-detail'),
    path('orders/create/', OrderView.as_view(), name='order-create'),
    path('orders/<int:pk>/update/', OrderView.as_view(), name='order-update'),
    path('orders/<int:pk>/delete/', OrderView.as_view(), name='order-delete'),
    path('order-items/', OrderItemView.as_view(), name='order-item-list'),
    path('order-items/<int:pk>/', OrderItemView.as_view(), name='order-item-detail'),
    path('orders/<int:order_pk>/items/create/', OrderItemView.as_view(), name='order-item-create'),
    path('order-items/<int:pk>/update/', OrderItemView.as_view(), name='order-item-update'),
    path('order-items/<int:pk>/delete/', OrderItemView.as_view(), name='order-item-delete'),
    path('carts/', CartView.as_view(), name='cart-list'),
    path('carts/<int:pk>/', CartView.as_view(), name='cart-detail'),
    path('carts/create/', CartView.as_view(), name='cart-create'),
    path('carts/<int:pk>/update/', CartView.as_view(), name='cart-update'),
    path('carts/<int:pk>/delete/', CartView.as_view(), name='cart-delete'),
    path('cart-items/', CartItemView.as_view(), name='cart-item-list'),
    path('cart-items/<int:pk>/', CartItemView.as_view(), name='cart-item-detail'),
    path('carts/<int:cart_pk>/items/add/', CartItemView.as_view(), name='cart-item-add'),
    path('cart-items/<int:pk>/update/', CartItemView.as_view(), name='cart-item-update'),
    path('carts/<int:cart_pk>/items/remove/<int:item_pk>/', CartItemView.as_view(), name='cart-item-remove')
]
