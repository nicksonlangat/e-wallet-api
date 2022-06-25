from django.db.models.signals import post_save, pre_delete
from .models import User
from django.dispatch import receiver
from core.models import Wallet
 
 
@receiver(post_save, sender=User)
def create_wallet(sender, instance, created, **kwargs):
    if created:
        Wallet.objects.create(user=instance)
  