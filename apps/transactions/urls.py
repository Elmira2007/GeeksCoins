from rest_framework.routers import DefaultRouter
from django.urls import path

from apps.transactions.views import TransactionsAPIViews

router = DefaultRouter()
router.register('', TransactionsAPIViews, 'api_transactions')

urlpatterns = router.urls
