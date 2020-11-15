from django.urls import path
from .views import (
    ProfileListView,
    UserProfileDetailView,
    ProfileDetailView,
    ProfileUpdate,
    ProfileDestroy,
    SponsoredProfileListView,
    UserFollowingListView,
    UserFollowingCreateView,
    UserFollowingDetailView,
    UserFollowingDeleteView,
    CurrentUserFollowers,
    CurrentUserFollowing,
    FollowingDetailView
)

urlpatterns = [
    path('profiles/', ProfileListView.as_view(), name='profiles'),
    path('userprofile/<pk>/detail/', UserProfileDetailView.as_view(), name='user-profile-detail'),
    path('profile/<pk>/detail/', ProfileDetailView.as_view(), name='profile-detail'),
    path('profile/<pk>/update/', ProfileUpdate.as_view(), name='profile-detail'),
    path('profile/<pk>/delete/', ProfileDestroy.as_view(), name='profile-delete'),
    path('followlist/', UserFollowingListView.as_view(), name='follow'),
    path('follow_user/', UserFollowingCreateView.as_view(), name='follow-user'),
    path('following/<pk>/details/', UserFollowingDetailView.as_view(), name='following-details'),
    path('following/<pk>/delete/', UserFollowingDeleteView.as_view(), name='delete-following'),
    path('followers/', CurrentUserFollowers.as_view(), name='followers'),
    path('user_following/', CurrentUserFollowing.as_view(), name='following'),
    path('account_followers/', FollowingDetailView.as_view(), name='account-followers'),
    path('sponsored/', SponsoredProfileListView.as_view(), name='sponsored-profile')
]