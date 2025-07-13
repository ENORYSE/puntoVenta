# signals.py
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .groups import assign_user_to_group

User = get_user_model()
    
@receiver(post_save, sender=User)
def assign_default_group(sender, instance, created, **kwargs):
    if created:
        assign_user_to_group(instance, 'customer')  # or logic to choose group