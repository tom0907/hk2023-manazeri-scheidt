
from django.db import models

# Create your models here.

class Users(models.Model):
    UserId = models.AutoField(primary_key=True)
    UserName = models.CharField(max_length=20)
    UserAddress = models.CharField(max_length=50, blank=True)
    UserDescription = models.CharField(max_length=300, blank=True)
    UserEvents = models.CharField(max_length=1000, blank=True)
    UserFavorites = models.CharField(max_length=1000, blank=True)
    UserFriends = models.CharField(max_length=1000, blank=True)
    UserOwnedEvents = models.CharField(max_length=1000, blank=True)

