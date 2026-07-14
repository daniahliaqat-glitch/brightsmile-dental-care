"""
Dashboard app views.

Handles the Patient Dashboard (upcoming appointments, history, profile,
favorite services, notifications) and the Admin Dashboard (overview of
doctors, services, appointments, patients, reviews, contact messages,
and newsletter subscribers).
"""

from datetime import date

from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render

from appointments.models import Appointment
from .models import Notification

from doctors.models import Doctor
from services.models import Service
from testimonials.models import Testimonial
from contact_us.models import ContactMessage
from newsletter.models import NewsletterSubscriber
from django.contrib.auth.models import User


@login_required
def patient_dashboard_view(request):
    """Render the logged-in patient's personal dashboard."""
    today = date.today()

    upcoming_appointments = Appointment.objects.filter(
        patient=request.user,
        appointment_date__gte=today,
    ).exclude(status='cancelled')

    appointment_history = Appointment.objects.filter(
        patient=request.user,
        appointment_date__lt=today,
    )

    favorite_appointments = Appointment.objects.filter(
        patient=request.user,
        is_favorite=True,
    )

    notifications = Notification.objects.filter(patient=request.user)[:10]

    context = {
        'upcoming_appointments': upcoming_appointments,
        'appointment_history': appointment_history,
        'favorite_appointments': favorite_appointments,
        'notifications': notifications,
        'unread_notification_count': notifications.filter(is_read=False).count(),
    }
    return render(request, 'dashboard/patient_dashboard.html', context)


def _is_staff_user(user):
    """Return True if the given user is allowed to view the admin dashboard."""
    return user.is_authenticated and user.is_staff


@user_passes_test(_is_staff_user, login_url='accounts:login')
def admin_dashboard_view(request):
    """Render the staff-only Admin Dashboard overview page."""
    context = {
        'doctor_count': Doctor.objects.count(),
        'service_count': Service.objects.count(),
        'appointment_count': Appointment.objects.count(),
        'pending_appointment_count': Appointment.objects.filter(status='pending').count(),
        'patient_count': User.objects.filter(is_staff=False).count(),
        'pending_review_count': Testimonial.objects.filter(is_approved=False).count(),
        'unread_message_count': ContactMessage.objects.filter(is_read=False).count(),
        'subscriber_count': NewsletterSubscriber.objects.filter(is_active=True).count(),
        'recent_appointments': Appointment.objects.all()[:8],
        'recent_messages': ContactMessage.objects.all()[:5],
    }
    return render(request, 'dashboard/admin_dashboard.html', context)