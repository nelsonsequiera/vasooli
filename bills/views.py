from rest_framework import generics
from .serializers import BillSerializer
from .models import Bill
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core import serializers


class BillsCreateView(generics.CreateAPIView):
    serializer_class = BillSerializer


class BillsDetailView(generics.RetrieveAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer


class BillsUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer


class BillsListView(generics.ListAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer


class BillsDeleteView(generics.DestroyAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer

    def get(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class BillUserList(generics.ListAPIView):
    serializer_class = BillSerializer
    user = ''

    def get_queryset(self):
        print self.user
        return Bill.objects.filter(user=self.user)
