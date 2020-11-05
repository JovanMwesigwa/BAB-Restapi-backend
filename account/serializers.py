from rest_framework import serializers
from .models import Profile, SponsoredProfile


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'user', 'location', 'description', 'contact', 'profile_type', 'working_hours', 'working_days','profile_pic', 'cover_photo']
        depth = 2


class SponsoredProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = SponsoredProfile
        fields = ['id', 'sponsored_profile', ]
        depth = 2

