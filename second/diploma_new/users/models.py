from django.db import models
from django.contrib.auth.models import User
from realtors.models import Realtor



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=500, blank=True)
    username = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=200, blank=True)
    profile_image = models.ImageField(upload_to="profiles/", default="profiles/user-default.png", blank=True)
    # realt = models.OneToOneField(Realtor, default=1, on_delete=models.CASCADE)
    realt = models.ForeignKey(Realtor, default=1, on_delete=models.CASCADE)


    def __str__(self):
        return self.username
from django.db import models


# Create your models here.
