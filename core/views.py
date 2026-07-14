"""
Core app views.

Handles Home, About Us, FAQ, Gallery, Pricing, Privacy Policy,
Terms & Conditions, and the custom 404 error page.
"""

from django.shortcuts import render

from .models import WhyChooseUsFeature, ClinicStat, GalleryImage, FAQ
from doctors.models import Doctor
from services.models import Service
from testimonials.models import Testimonial
from blog.models import BlogPost
from insurance.models import InsurancePartner


def home_view(request):
    """Render the homepage with all featured sections."""
    context = {
        'features': WhyChooseUsFeature.objects.filter(is_active=True),
        'stats': ClinicStat.objects.filter(is_active=True),
        'doctors': Doctor.objects.filter(is_active=True)[:4],
        'services': Service.objects.filter(is_active=True)[:8],
        'testimonials': Testimonial.objects.filter(is_approved=True)[:6],
        'insurance_partners': InsurancePartner.objects.filter(is_active=True),
        'articles': BlogPost.objects.filter(is_published=True)[:3],
    }
    return render(request, 'core/home.html', context)


def about_view(request):
    """Render the About Us page."""
    context = {
        'stats': ClinicStat.objects.filter(is_active=True),
        'features': WhyChooseUsFeature.objects.filter(is_active=True),
    }
    return render(request, 'core/about.html', context)


def faq_view(request):
    """Render the FAQ page, grouped by category."""
    faqs = FAQ.objects.filter(is_active=True)
    context = {
        'general_faqs': faqs.filter(category='general'),
        'appointment_faqs': faqs.filter(category='appointments'),
        'insurance_faqs': faqs.filter(category='insurance'),
        'billing_faqs': faqs.filter(category='billing'),
    }
    return render(request, 'core/faq.html', context)


def gallery_view(request):
    """Render the Gallery page with optional category filtering."""
    category = request.GET.get('category', 'all')
    images = GalleryImage.objects.filter(is_active=True)

    if category != 'all':
        images = images.filter(category=category)

    context = {
        'images': images,
        'selected_category': category,
        'categories': GalleryImage.CATEGORY_CHOICES,
    }
    return render(request, 'core/gallery.html', context)


def pricing_view(request):
    """Render the Pricing page listing all active services and their demo prices."""
    context = {
        'services': Service.objects.filter(is_active=True),
    }
    return render(request, 'core/pricing.html', context)


def privacy_policy_view(request):
    """Render the static Privacy Policy page."""
    return render(request, 'core/privacy_policy.html')


def terms_conditions_view(request):
    """Render the static Terms & Conditions page."""
    return render(request, 'core/terms_conditions.html')


def custom_404_view(request, exception=None):
    """Render the custom 404 error page."""
    return render(request, 'core/404.html', status=404)