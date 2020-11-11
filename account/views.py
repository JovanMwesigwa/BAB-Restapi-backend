from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Profile, SponsoredProfile, UserFollowing
from .serializers import ProfileSerializer, SponsoredProfileSerializer, UserFollowingSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status


class ProfileListView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    pagination_class = PageNumberPagination


class UserProfileDetailView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = ['user']

    def get_object(self):
        return Profile.objects.get(user=self.request.user)


class ProfileDetailView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileUpdate(generics.UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    parser_classes = (FormParser, MultiPartParser, JSONParser)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        current_user = self.request.user
        if current_user == instance.user:
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


class ProfileDestroy(generics.DestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class UserFollowingListView(generics.ListAPIView):
    queryset = UserFollowing.objects.all()
    serializer_class = UserFollowingSerializer


class UserFollowingCreateView(generics.CreateAPIView):
    queryset = UserFollowing.objects.all()
    serializer_class = UserFollowingSerializer

    def perform_create(self, serializer):
        serializer.save(user_from=self.request.user.profile)


# ************** User following activity logic***************

class UserFollowingDeleteView(generics.DestroyAPIView):
    queryset = UserFollowing.objects.all()
    serializer_class = UserFollowingSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance_user = instance.user_from
        current_user = self.request.user.profile

        if instance_user == current_user:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


# ****************User following retrieve logic ***************

class UserFollowingDetailView(generics.RetrieveAPIView):
    queryset = UserFollowing.objects.all()
    serializer_class = UserFollowingSerializer


class CurrentUserFollowers(generics.ListAPIView):
    queryset = UserFollowing.objects.all()
    serializer_class = UserFollowingSerializer

    def get_queryset(self):
        current_user = self.request.user.profile
        followers = current_user.followers.all()
        return followers


class SponsoredProfileListView(generics.ListAPIView):
    queryset = SponsoredProfile.objects.all()
    serializer_class = SponsoredProfileSerializer

