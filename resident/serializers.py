from rest_framework import serializers

from .models import Resident, ResidentPhotos

class ResidentPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResidentPhotos
        fields = ('id', 'photo')

class ResidentSerializer(serializers.ModelSerializer):
    photos = ResidentPhotoSerializer(many=True, read_only=True)
    class Meta:
        model = Resident
        fields = ('id', 'responsible', 'name', 'description', 'direction', 'photos')