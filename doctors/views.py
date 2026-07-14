"""
Doctors app views.

Handles the doctor listing page and individual doctor profile pages.
"""

from django.shortcuts import render, get_object_or_404

from .models import Doctor
from services.models import Service


def doctor_list_view(request):
    """Render the 'Our Dentists' listing page."""
    context = {
        'doctors': Doctor.objects.filter(is_active=True),
    }
    return render(request, 'doctors/doctor_list.html', context)


def doctor_detail_view(request, slug):
    """Render an individual doctor's profile page."""
    doctor = get_object_or_404(Doctor, slug=slug, is_active=True)
    context = {
        'doctor': doctor,
        'services': Service.objects.filter(is_active=True),
    }
    return render(request, 'doctors/doctor_detail.html', context)