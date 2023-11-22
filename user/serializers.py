from rest_framework import serializers

from .models import User

class UserSerializerFull(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'full_name', 'organization', 'phone', 'user_type')