from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('users.urls')),
	path("product/", include("product.urls")),
    path('shopping_cart/', include('shopping_cart.urls')),
]
