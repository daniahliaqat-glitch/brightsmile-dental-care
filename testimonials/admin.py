"""
Admin configuration for the testimonials app.
"""

from django.contrib import admin
from .models import Testimonial


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('patient_name', 'rating', 'is_approved', 'created_at')
    list_editable = ('is_approved',)
    list_filter = ('is_approved', 'rating')
    search_fields = ('patient_name', 'review_text')
    date_hierarchy = 'created_at'