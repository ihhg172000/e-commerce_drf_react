from rest_framework import serializers
from .models import Product, Brand, Category
from users.models import User

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__" 

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="category.name", read_only=True, label="Category Name")
    brand_name = serializers.CharField(source ="brand.name", read_only=True, label="Brand Name")
    first_name = serializers.CharField(source="user.first_name", read_only=True, label="User Last Name")
    

    class Meta:
        model = Product
        fields = ['id',  'name', 'description', 'price', 'category_name', 'brand_name', 'quantity', 'created_at', 'updated_at', 'first_name']
