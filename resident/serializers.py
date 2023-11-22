from rest_framework import serializers
from taggit.serializers import TagListSerializerField, TaggitSerializer

from .models import Resident, ResidentPhotos

class ResidentPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResidentPhotos
        fields = ('id', 'photo')

class ResidentSerializer(TaggitSerializer, serializers.ModelSerializer):
    photos = ResidentPhotoSerializer(many=True, read_only=True)
    tags = TagListSerializerField()
    class Meta:
        model = Resident
        fields = ('id', 'responsible', 'name', 'description', 'direction', 'floor', 'photos', 'tags')