from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    phone = PhoneNumberField(_('phone'), unique=True)
    first_name = models.CharField(_('first name'), max_length=128)
    last_name = models.CharField(_('last name'), max_length=128)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff'), default=False)
    is_superuser = models.BooleanField(_("superuser"), default=False)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'phone',
        'first_name',
        'last_name'
    ]

    objects = UserManager()

    def __str__(self):
        return self.email


class Address(models.Model):
    country = models.CharField(_('country'), max_length=128)
    state = models.CharField(_('state'), max_length=128)
    city = models.CharField(_('city'), max_length=128)
    street = models.CharField(_('street'), max_length=128)
    zip_code = models.IntegerField(_('zip code'))
    created_at = models.DateField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.first_name} {self.user. last_name}, \
            {self.street}, {self.city}, {self.state} {self.zip_code}, {self.country}'
