from .models import User
from rest_framework import serializers
from django.core import exceptions
from rest_framework_jwt.settings import api_settings
import django.contrib.auth.password_validation as validators


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'is_superuser', 'first_name', 'last_name', 'email', 'is_manager', 'is_active')


class RegisterUserSerializer(serializers.ModelSerializer):

    def to_representation(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return {
            'username': obj.username,
            'password': obj.password,
            'token': token
        }

    def validate(self, data):
        # here data has all the fields which have validated values
        # so we can create a User instance out of it
        user = User(**data)

        # get the password from the data
        password = data.get('password')

        errors = dict()
        try:
            # validate the password and catch the exception
            validators.validate_password(password=password, user=User)

        # the exception raised here is different than serializers.ValidationError
        except exceptions.ValidationError as e:
            errors['password'] = list(e.messages)

        if errors:
            raise serializers.ValidationError(errors)

        return super(RegisterUserSerializer, self).validate(data)

    class Meta:
        model = User
        fields = ('username', 'password')
