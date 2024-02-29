from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import  CreateAPIView, ListAPIView
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated, AllowAny

from apps.users.models import User, UserCoins
from apps.users.serializers import UserDetailSerializer, UserRegisterSerializer, UserSerializer,CoinInfoSerializer
from apps.users.permissions import UserPermissons
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.response import Response
from django.contrib.auth.models import AnonymousUser
from rest_framework import status

class UserAPIViewsSet(GenericViewSet,
                      mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = IsAuthenticated

    def get_serializer_class(self):
        if self.action == 'create':
            return UserRegisterSerializer
        if self.action == 'retrieve':
            return UserDetailSerializer
        return UserSerializer
    
    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            return (UserPermissons(),)
        return (AllowAny(), )
    
    def perform_update(self, serializer):
        return serializer.save(user = self.request.user)
    

class UserRegisterAPI(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer


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