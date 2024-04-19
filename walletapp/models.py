from django.db import models

# Create your models here.

class WalletType(models.Model) :
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name
class Users(models.Model) :
    phonenumber = models.IntegerField()
    wallettype = models.ForeignKey(WalletType, on_delete=models.CASCADE, related_name='user_wallettype_rel')
    amount = models.DecimalField(max_digits=10000, decimal_places=2, default=0.00)

    def __str__(self):
        return str(self.phonenumber)+'('+str(self.wallettype.name)+')'

class Transaction(models.Model) :
    TransactiontypeList = [
        ('credit', 'credit'),
        ('debit', 'debit')
    ]
    transactiontype = models.CharField(max_length=100,choices=TransactiontypeList)
    transactiondate = models.DateTimeField(auto_now=True)
    amount = models.DecimalField(max_digits=1000, decimal_places=2)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='user_transaction_rel')

