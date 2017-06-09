import requests
from urlparse import urlparse
from django.db import IntegrityError
from django.urls import reverse
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer
from .models import User


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint to allow users to interact.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': UserSerializer(user, context={'request': request}).data
    }


class SignUpView(APIView):

    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):

        username = request.data.get('username')
        password = request.data.get('password')
        password2 = request.data.get('confirm_password')
        response = {}
        if username and password == password2:
            try:
                User.objects.create_user(
                    username=username,
                    password=password,
                    email=username
                ).save()
                scheme = urlparse(request.build_absolute_uri()).scheme
                url = scheme + '://' + request.META['HTTP_HOST'] + reverse('create_token')
                data = {'username': username, 'password': password}
                response = requests.post(url, data=data).json()

            except IntegrityError as e:
                response['token'] = ''
                response['message'] = 'User alredy exists, please register with a different user name.'

        return Response(response)
