from django.urls import path
from .views import AuthenticatedUserRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('me/', AuthenticatedUserRetrieveUpdateDestroyAPIView.as_view())
]
