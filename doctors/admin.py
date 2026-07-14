"""
Admin configuration for the doctors app.
"""

from django.contrib import admin
from .models import Doctor


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'specialization', 'years_of_experience', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    search_fields = ('full_name', 'specialization')
    list_filter = ('is_active', 'specialization')
    prepopulated_fields = {'slug': ('full_name',)}