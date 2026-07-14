"""
Admin configuration for the dashboard app.
"""

from django.contrib import admin
from .models import Notification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'patient', 'notification_type', 'is_read', 'created_at')
    list_editable = ('is_read',)
    list_filter = ('notification_type', 'is_read')
    search_fields = ('title', 'message', 'patient__username')
    date_hierarchy = 'created_at'