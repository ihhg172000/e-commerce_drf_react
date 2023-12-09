from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.generics import (
    CreateAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.permissions import IsAuthenticated
from .models import Address
from .serializers import (
    UserSerializer,
    AddressSerializer
)


User = get_user_model()


class RegisterAPIView(
    CreateAPIView
):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class UserRetrieveUpdateDestroyAPIView(
    RetrieveUpdateDestroyAPIView
):
    serializer_class = UserSerializer
    permission_classes = [
        IsAuthenticated
    ]

    def get_object(self):
        return self.request.user
    

class UserAddressesListCreateAPIView(
    ListCreateAPIView
):
    serializer_class = AddressSerializer
    permission_classes = [
        IsAuthenticated
    ]

    def get_queryset(self):
        user = self.request.user
        return Address.objects.all().filter(user=user)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = AddressSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.validated_data.setdefault('user_id', request.user.id)
            serializer.save()
            return Response(serializer.validated_data)
        

class UserAddressRetrieveUpdateDestroyAPIView(
    RetrieveUpdateDestroyAPIView
):
    serializer_class = AddressSerializer
    permission_classes = [
        IsAuthenticated
    ]

    def get_queryset(self):
        return Address.objects.all().filter(user=self.request.user)