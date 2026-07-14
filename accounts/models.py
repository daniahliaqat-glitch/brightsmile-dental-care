"""
Accounts app models.

Extends the built-in Django User model with a PatientProfile,
storing additional patient-specific information such as phone
number, date of birth, and profile picture.
"""

from django.conf import settings
from django.db import models


class PatientProfile(models.Model):
    """Additional profile information for a registered patient."""

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='patient_profile',
    )
    phone = models.CharField(max_length=20, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=255, blank=True)
    profile_picture = models.ImageField(
        upload_to='patients/',
        blank=True,
        null=True,
    )

    email_notifications = models.BooleanField(default=True)
    sms_notifications = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Patient Profile'
        verbose_name_plural = 'Patient Profiles'

    def __str__(self):
        return f"Profile: {self.user.get_full_name() or self.user.username}"