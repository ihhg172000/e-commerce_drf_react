from django.urls import path
from . import views


urlpatterns = [
    path('users/', views.CustomUserListCreateAPIView.as_view()),
    path('users/<int:pk>/', views.CustomUserRetrieveUpdateDestroyAPIView.as_view())
]
