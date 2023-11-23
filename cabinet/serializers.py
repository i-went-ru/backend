from rest_framework import serializers

from resident.serializers import ResidentSerializer
from .models import Cabinet

class CabinetSerializer(serializers.ModelSerializer):
    resident = ResidentSerializer()
    class Meta:
        model = Cabinet
        fields = ('id', 'resident', 'cabinet_number', 'color', 'path')