"""
Admin configuration for the services app.
"""

from django.contrib import admin
from .models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon', 'price', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    search_fields = ('name', 'short_description')
    list_filter = ('is_active', 'icon')
    prepopulated_fields = {'slug': ('name',)}