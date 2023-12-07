from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Address


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'phone',
            'first_name',
            'last_name',
            'password'
        ]
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        try:
            password = validated_data.pop('password')
            instance.set_password(password)
            instance.save()
        except Exception:
            pass
        return super().update(instance, validated_data)


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
            'id',
            'country',
            'state',
            'city',
            'street',
            'zip_code'
        ]
