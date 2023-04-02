from rest_framework import serializers
from HackApp.models import Users,Events,Comments
from django.contrib.auth.models import User

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Users 
        fields=('UserId','UserName','UserAddress','UserDescription','UserEvents','UserFavorites','UserFriends','UserOwnedEvents')

