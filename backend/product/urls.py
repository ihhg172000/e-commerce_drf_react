from django.urls import path

from . import views

urlpatterns = [
    path("products/", views.get_all_products, name="products"),
	path("products/<str:id>", views.get_product_by_id, name="get_by_id_product"),
	path("categories/", views.get_all_categories, name="get_all_categories"),
	path("brands/", views.get_all_brands, name="get_all_categories"),

]