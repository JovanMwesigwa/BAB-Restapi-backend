from django.contrib import admin
from .models import Profile, ProfileType, SponsoredProfile, UserFollowing
# Register your models here.


admin.site.register(Profile)
admin.site.register(ProfileType)
admin.site.register(SponsoredProfile)
admin.site.register(UserFollowing)

