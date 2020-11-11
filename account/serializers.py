from rest_framework import serializers
from .models import Profile, SponsoredProfile, UserFollowing


class UserFollowingSerializer(serializers.ModelSerializer):
    user_from = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = UserFollowing
        fields = ['id', 'user_to', 'user_from', 'created']
        # depth = 1

    # def create(self, validated_data):
    #     return UserFollowing.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.user_from = validated_data.get('user_from', instance.profile)
    #     return instance


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'user', 'location', 'description', 'contact', 'profile_type', 'following', 'working_hours', 'working_days','profile_pic', 'cover_photo']
        depth = 2


class SponsoredProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = SponsoredProfile
        fields = ['id', 'sponsored_profile', ]
        depth = 2

