from rest_framework import serializers
from walletapp import models
import re
from wallet.settings import MINIMUM_WALLET_BALANCE


class WalletTypeSerializers(serializers.ModelSerializer) :
    class Meta :
        model = models.WalletType
        fields = '__all__'

class UserSerializers(serializers.ModelSerializer) :
    wallettype_name = serializers.SerializerMethodField(read_only=True, required=False)

    def validate(self, attrs):
        pnumber = attrs.get('phonenumber')
        wallettype = attrs.get('wallettype')
        pattern = re.compile(r'[6-9][0-9]{9}$')
        if not pattern.match(str(pnumber)) :
            raise serializers.ValidationError({'phonenumber': 'Please enter valid phone number'})
        if models.Users.objects.filter(phonenumber=pnumber, wallettype=wallettype).exists() :
            raise serializers.ValidationError({'phonenumber': 'User already registered for this wallet type'})
        return attrs


    def get_wallettype_name(self, value):
        return value.wallettype.name

    class Meta :
        model = models.Users
        fields = '__all__'

class TransactionSerializers(serializers.ModelSerializer) :
    user = UserSerializers()
    date_format = serializers.DateTimeField(source='transactiondate', format='%Y-%m-%d %H:%M:%S')
    class Meta :
        model = models.Transaction
        fields = '__all__'

class CreditTransactionSerializers(serializers.ModelSerializer) :

    def validate(self, attrs):
        ttype = attrs.get('transactiontype')
        if ttype != 'credit' :
            raise serializers.ValidationError({'transactiontype': 'Transactiontype must be Credit'})
        amount = attrs.get('amount')
        if amount and amount <= 0 :
            raise serializers.ValidationError({'amount': 'Amount can`t be -ve value'})
        return attrs

    class Meta :
        model = models.Transaction
        fields = '__all__'

class DebitTransactionSerializers(serializers.ModelSerializer) :

    def validate(self, attrs):
        ttype = attrs.get('transactiontype')
        if ttype != 'debit' :
            raise serializers.ValidationError({'transactiontype': 'Transactiontype must be Debit'})
        amount = attrs.get('amount')
        if amount and amount <= 0 :
            raise serializers.ValidationError({'amount': 'Amount can`t be -ve value'})
        userobj = models.Users.objects.get(id=attrs.get('user').id)
        if not userobj :
            raise serializers.ValidationError({'user': 'Please enter valid user details'})
        if userobj and userobj.amount < 0 :
            raise serializers.ValidationError({'amount': 'wallet is not having minimum balance'})
        if userobj and userobj.amount > 0 and (userobj.amount - amount) <= MINIMUM_WALLET_BALANCE :
            raise serializers.ValidationError({'amount': 'Can`t debit due to low balance' })
        return attrs

    class Meta :
        model = models.Transaction
        fields = '__all__'