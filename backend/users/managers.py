from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, email, password, **other_fields):
        """
        Creates and saves a user with the given email and password.
        """
        if not email:
            raise ValueError(_('Users must have an email address'))
        user = self.model(
            email=self.normalize_email(email),
            **other_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **other_fields):
        """
        Creates and saves a superuser with the given email and password.
        """
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        
        return self.create_user(email, password, **other_fields)
