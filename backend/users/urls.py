from django.urls import path
from .views import (
    RegisterAPIView,
    AuthenticatedUserRetrieveUpdateDestroyAPIView
)


urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('me/', AuthenticatedUserRetrieveUpdateDestroyAPIView.as_view())
]
