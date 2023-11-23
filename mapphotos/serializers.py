from rest_framework import serializers

from .models import MapPhoto

class MapPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MapPhoto
        fields = ('x', 'y', 'color', 'image')