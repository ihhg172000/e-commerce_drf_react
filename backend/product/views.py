from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer, CategorySerializer, BrandSerializer
from .models import Product, Category, Brand
from django.shortcuts import get_object_or_404

"""product get requests"""
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


"""category get requests"""
@api_view(['GET'])
def get_all_categories(request):
	categories = Category.objects.all()
	cat_serializer = CategorySerializer(categories, many=True)
	return Response({"Categories": cat_serializer.data})

"""brands get requests"""
@api_view(['GET'])
def get_all_brands(request):
	brands = Brand.objects.all()
	brand_serializer = BrandSerializer(brands, many=True)
	return Response({"Brands": brand_serializer.data})