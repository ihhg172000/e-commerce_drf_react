from django.shortcuts import render
from .models import Order
# Create your views here.

def index(request):
    # diplay all orders created
    orders = Order.objects.all()
    return render(request, 'orders/order_list.html', {
        'orders': orders,
    })
