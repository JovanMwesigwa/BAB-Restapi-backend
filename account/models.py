from django.db import models
from django.conf import settings


# Create your models here.

class ProfileType(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    location = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    profile_type = models.ForeignKey(ProfileType, on_delete=models.CASCADE, default=17)
    profile_pic = models.ImageField(upload_to='users/profile_pics/%Y/%m/%d/', blank=True)
    cover_photo = models.ImageField(upload_to='users/cover_photos/%Y/%m/%d/', blank=True)
    contact = models.CharField(max_length=255, null=True, blank=True)
    working_days = models.CharField(max_length=100, null=True, blank=True)
    working_hours = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return 'Profile for {}'.format(self.user.username)
    
    
class SponsoredProfile(models.Model):
    sponsored_profile = models.ManyToManyField(Profile)

