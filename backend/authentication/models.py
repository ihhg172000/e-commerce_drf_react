from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    # Add any additional fields you need
    email = models.EmailField(unique=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        related_query_name='user',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )

    # Specify a different related_name for user_permissions
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        related_query_name='user',
        blank=True,
        help_text='Specific permissions for this user.',
    )
