from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product
from django.shortcuts import get_object_or_404


@api_view(['GET'])
def get_all_products(request):
	products = Product.objects.all()
	serializer  = ProductSerializer(products, many=True)
	return Response({"products": serializer.data})
	

@api_view(['GET'])
def get_product_by_id(request, id):
	products = get_object_or_404(Product, id=id)
	serializer  = ProductSerializer(products, many=False)
	return Response({"product": serializer.data})

