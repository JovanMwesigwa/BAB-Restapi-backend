from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'user', 'location', 'description', 'contact', 'profile_type', 'profile_pic', 'cover_photo']
        depth = 2