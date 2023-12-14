from django.urls import path

from . import views

urlpatterns = [
    path("products/", views.get_all_products, name="products"),
	path("products/<str:id>", views.get_product_by_id, name="get_by_id_product"),

]