from django.db import models
from accounts.models import User
import math, random
from uuid import uuid4
# Create your models here.

TYPE_CHOICES = (
    ("Deposit", "Deposit"),
    ("Withdrawal", "Withdrawal")
)

class Wallet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wallet_owner')
    account_number = models.CharField(max_length=255, null=True, blank=True)
    wallet_balance = models.DecimalField(max_digits=9, decimal_places=2,default=0)
    date_created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        val = math.floor(1000000 + random.random()*9000000)
        self.account_number=str(val*9)
        super(Wallet, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.account_number)
    
    class Meta:
        ordering = ['-date_created', ]
    
    
class Transaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_user')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_user')
    transaction_type = models.CharField(choices=TYPE_CHOICES,max_length=20)
    amount = models.DecimalField(max_digits=9, decimal_places=2,default=0)
    transaction_code = models.CharField(max_length=255, null=True, blank=True)
    transaction_date = models.DateTimeField(auto_now_add=True)
    is_successful = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        val = math.floor(10000 + random.random()*90000)
        self.transaction_code='TRN'+str(val*9)
        super(Transaction, self).save(*args, **kwargs)
    
    class Meta:
        ordering = ['-transaction_date', ]

    def __str__(slef):
        return str(self.transaction_code)
    


