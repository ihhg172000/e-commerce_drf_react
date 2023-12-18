from django.urls import path
from .views import OrderView, OrderItemView, CartView, CartItemView

app_name = 'cart'

urlpatterns = [
    path('orders/', OrderView.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderView.as_view(), name='order-detail'),
    path('orders/create/', OrderView.as_view(), name='order-create'),
    path('orders/<int:pk>/update/', OrderView.as_view(), name='order-update'),
    path('orders/<int:pk>/delete/', OrderView.as_view(), name='order-delete')
]
