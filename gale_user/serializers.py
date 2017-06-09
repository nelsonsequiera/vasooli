from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'is_superuser', 'first_name', 'last_name', 'email', 'is_manager', 'is_active')
