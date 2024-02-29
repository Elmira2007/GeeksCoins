# coins/views.py
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.response import Response
from apps.coins.models import UserCoins
from apps.coins.serialiaers import CoinInfoSerializer
from django.contrib.auth.models import AnonymousUser
from rest_framework import status

# Create your views here.
class CoinInfoAPIView(GenericViewSet, mixins.ListModelMixin):
    serializer_class = CoinInfoSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            user_coins, created = UserCoins.objects.get_or_create(user = self.request.user)
            return [user_coins] 
        else:
            return []

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)


