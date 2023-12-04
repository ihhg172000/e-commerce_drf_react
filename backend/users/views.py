from django.contrib.auth import get_user_model
from rest_framework.generics import (
    CreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer


User = get_user_model()


class RegisterAPIView(
    CreateAPIView
):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class AuthenticatedUserRetrieveUpdateDestroyAPIView(
    RetrieveUpdateDestroyAPIView
):
    serializer_class = UserSerializer
    permission_classes = [
        IsAuthenticated
    ]

    def get_object(self):
        return self.request.user
