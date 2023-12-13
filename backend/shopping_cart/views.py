from django.shortcuts import render
from .models import Order
# Create your views here.

def index(request):
    # diplay all orders created
    orders = Order.objects.all()
    return render(request, 'orders/order_list.html', {
        'orders': orders,
    })

def order_detail(request, order_id):
    order = Order.objects.filter(pk=order_id).first()
    return render(request, 'order/order_detail.html', {
        'order': order
    })

