"""
Services app views.

Handles the services listing page and individual service detail pages.
"""

from django.shortcuts import render, get_object_or_404

from .models import Service
from doctors.models import Doctor


def service_list_view(request):
    """Render the 'Our Services' listing page."""
    context = {
        'services': Service.objects.filter(is_active=True),
    }
    return render(request, 'services/service_list.html', context)


def service_detail_view(request, slug):
    """Render an individual service's detail page."""
    service = get_object_or_404(Service, slug=slug, is_active=True)
    context = {
        'service': service,
        'doctors': Doctor.objects.filter(is_active=True)[:4],
        'related_services': Service.objects.filter(is_active=True).exclude(slug=slug)[:3],
    }
    return render(request, 'services/service_detail.html', context)