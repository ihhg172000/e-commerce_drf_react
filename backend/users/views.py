from rest_framework import generics
from .models import CustomUser
from .serializers import CustomUserSerializer


class CustomUserListCreateAPIView(
    generics.ListCreateAPIView
):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CustomUserRetrieveUpdateDestroyAPIView(
    generics.RetrieveUpdateDestroyAPIView
):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
