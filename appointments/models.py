"""
Appointments app models.

Handles patient appointment bookings, storing the patient's contact
details, chosen doctor, chosen service, and preferred date/time.
"""

from django.conf import settings
from django.db import models

from doctors.models import Doctor
from services.models import Service


class Appointment(models.Model):
    """A patient's booked or requested appointment."""

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    # Link to a registered patient account, if the booking was made while
    # logged in. Guest bookings are also allowed, so this is nullable.
    patient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='appointments',
    )

    full_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.SET_NULL,
        null=True,
        related_name='appointments',
    )
    service = models.ForeignKey(
        Service,
        on_delete=models.SET_NULL,
        null=True,
        related_name='appointments',
    )

    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    message = models.TextField(blank=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    is_favorite = models.BooleanField(
        default=False,
        help_text="Marked by the patient as a favorite service/booking."
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-appointment_date', '-appointment_time']
        verbose_name = 'Appointment'
        verbose_name_plural = 'Appointments'

    def __str__(self):
        return f"{self.full_name} - {self.appointment_date} {self.appointment_time}"