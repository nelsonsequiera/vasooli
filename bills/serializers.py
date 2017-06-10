from .models import Bill
from rest_framework import serializers
from gale_user.serializers import UserSerializer


class BillSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    manager = UserSerializer()

    class Meta:
        model = Bill
        fields = (
            'user', 'bill_date', 'project_id', 'description', 'amount', 'proof_image',
            'manager', 'is_save', 'is_submit', 'is_paid'
        )
