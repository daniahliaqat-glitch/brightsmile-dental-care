"""
Admin configuration for the appointments app.
"""

from django.contrib import admin
from .models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        'full_name', 'doctor', 'service', 'appointment_date',
        'appointment_time', 'status', 'created_at',
    )
    list_editable = ('status',)
    list_filter = ('status', 'appointment_date', 'doctor', 'service')
    search_fields = ('full_name', 'email', 'phone')
    date_hierarchy = 'appointment_date'