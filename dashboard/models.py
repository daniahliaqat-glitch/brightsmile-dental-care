"""
Dashboard app models.

Handles patient-facing notifications shown in the Patient Dashboard
(e.g. appointment reminders, confirmations, and system messages).
"""

from django.conf import settings
from django.db import models


class Notification(models.Model):
    """A notification message shown to a patient in their dashboard."""

    TYPE_CHOICES = [
        ('appointment', 'Appointment Update'),
        ('reminder', 'Reminder'),
        ('promotion', 'Promotion'),
        ('system', 'System Message'),
    ]

    patient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='notifications',
    )
    notification_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='system')
    title = models.CharField(max_length=150)
    message = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'

    def __str__(self):
        return f"{self.title} - {self.patient.username}"