import time

from django.shortcuts import get_object_or_404
from rest_framework import viewsets, filters
from walletapp import models
from . import serializers
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db import transaction
from rest_framework import mixins


class WalletTypeViewset(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet) :
    queryset = models.WalletType.objects.all()
    serializer_class = serializers.WalletTypeSerializers
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]

class userviewset(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet) :
    queryset = models.Users.objects.all()
    serializer_class = serializers.UserSerializers
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    multiple_lookup_fields = ['phonenumber']

    def create(self, request, *args, **kwargs):
        sser = serializers.UserSerializers(data=request.data)
        if sser.is_valid(raise_exception=True):
            sserobj = sser.save()
            return Response(sser.data)

    @action(detail=True,methods=['GET'])
    def balance(self, request, pk):
        obj = models.Users.objects.filter(phonenumber=pk)
        balance_dict={}
        for detail in obj :
            balance_dict[detail.wallettype.name] = detail.amount
        return Response(balance_dict)

class TransactionViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet) :
    queryset = models.Transaction.objects.all()
    serializer_class = serializers.TransactionSerializers
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filter_fields = [i.name for i in models.Transaction._meta.fields]

    def get_queryset(self):
        print(self.request.query_params.get('startdate', None))
        print(self.request.query_params.get('enddate', None))
        if self.request.query_params.get('startdate', None) :
            self.queryset = self.queryset.filter(transactiondate__gte=self.request.query_params.get('startdate', None)+' 00:00:00')
        if self.request.query_params.get('enddate', None) :
            self.queryset = self.queryset.filter(transactiondate__lte=self.request.query_params.get('enddate', None)+' 23:59:59')
        return self.queryset

    @action(detail=False, methods=['POST'])
    def credit(self, request):
        print(request.data)
        serobj = serializers.CreditTransactionSerializers(data=request.data)
        if serobj.is_valid(raise_exception=True) :
            with transaction.atomic() :
                print("serobj.validated_data", serobj.validated_data)
                tobj = models.Transaction.objects.create(**serobj.validated_data)
                print(tobj, tobj.user, tobj.user.amount)
                tobj.user.amount = tobj.user.amount + tobj.amount
                tobj.user.save()
            return Response(serobj.data)

    @action(detail=False, methods=['POST'])
    def debit(self, request):
        print(request.data)
        serobj = serializers.DebitTransactionSerializers(data=request.data)
        if serobj.is_valid(raise_exception=True):
            with transaction.atomic():
                tobj = models.Transaction.objects.create(**serobj.validated_data)
                print(tobj, tobj.user, tobj.user.amount)
                tobj.user.amount = tobj.user.amount - tobj.amount
                tobj.user.save()
                transaction.mark_for_rollback_on_error()
            return Response(serobj.data)