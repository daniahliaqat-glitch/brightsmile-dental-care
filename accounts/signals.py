"""
Accounts app signals.

Automatically creates a PatientProfile whenever a new User is created,
so every registered patient always has an associated profile.
"""

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import PatientProfile


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_patient_profile(sender, instance, created, **kwargs):
    """Create a PatientProfile automatically when a new User is created."""
    if created:
        PatientProfile.objects.get_or_create(user=instance)