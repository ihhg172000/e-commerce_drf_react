from django.urls import path
from .views import (
    RegisterAPIView,
    UserRetrieveUpdateDestroyAPIView,
    UserAddressesListCreateAPIView,
    UserAddressRetrieveUpdateDestroyAPIView
)


urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('me/', UserRetrieveUpdateDestroyAPIView.as_view()),
    path('my_addresses/', UserAddressesListCreateAPIView.as_view()),
    path('my_addresses/<int:pk>', UserAddressRetrieveUpdateDestroyAPIView.as_view())
]
