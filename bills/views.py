from rest_framework import generics
from .serializers import BillSerializer
from .models import Bill


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
