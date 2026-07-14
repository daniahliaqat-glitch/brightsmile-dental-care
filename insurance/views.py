"""
Insurance app views.

Handles the Insurance page listing partners, accepted plans, and
insurance-related frequently asked questions.
"""

from django.shortcuts import render

from .models import InsurancePartner, AcceptedPlan
from core.models import FAQ


def insurance_view(request):
    """Render the Insurance page."""
    context = {
        'partners': InsurancePartner.objects.filter(is_active=True),
        'plans': AcceptedPlan.objects.filter(is_active=True),
        'insurance_faqs': FAQ.objects.filter(is_active=True, category='insurance'),
    }
    return render(request, 'insurance/insurance.html', context)