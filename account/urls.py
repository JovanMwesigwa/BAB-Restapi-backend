from django.urls import path
from .views import (
    ProfileListView,
    UserProfileDetailView,
    ProfileDetailView,
    ProfileUpdate,
    ProfileDestroy
)

urlpatterns = [
    path('profiles/', ProfileListView.as_view(), name='profiles'),
    path('userprofile/<pk>/detail/', UserProfileDetailView.as_view(), name='user-profile-detail'),
    path('profile/<pk>/detail/', ProfileDetailView.as_view(), name='profile-detail'),
    path('profile/<pk>/update/', ProfileUpdate.as_view(), name='profile-detail'),
    path('profile/<pk>/delete/', ProfileDestroy.as_view(), name='profile-delete'),
]