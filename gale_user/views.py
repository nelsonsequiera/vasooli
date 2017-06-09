from rest_framework import viewsets
from .serializers import UserSerializer
from .models import User


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint to allow users to interact.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
