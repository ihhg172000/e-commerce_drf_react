from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.index, name='index'),
    path('order/<int:order_id>', views.order_detail, name='order_detail'),
]