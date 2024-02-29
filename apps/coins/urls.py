from rest_framework.routers import DefaultRouter
from django.urls import path

from apps.coins.views import CoinInfoAPIView

router = DefaultRouter()
router.register('coin', CoinInfoAPIView, basename='api_coin')

urlpatterns = router.urls