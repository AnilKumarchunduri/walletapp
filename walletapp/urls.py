from django.contrib import admin
from django.urls import path, include
from walletapp.rest_api import viewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('wallettype', viewset.WalletTypeViewset)
router.register('users', viewset.userviewset)
router.register('transaction', viewset.TransactionViewset)


urlpatterns = [
]
urlpatterns += router.urls