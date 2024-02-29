# coins/serializers.py
from rest_framework import serializers
from apps.users.models import User

class CoinInfoSerializer(serializers.Serializer):
    username = serializers.CharField(source = 'user.username')
    balance = serializers.IntegerField()