"""
Appointments app views.

Handles booking a new appointment and showing a confirmation page.
"""

from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import AppointmentForm


def book_appointment_view(request):
    """Render the appointment booking form and handle submission."""
    initial = {}
    service_slug = request.GET.get('service')
    doctor_slug = request.GET.get('doctor')

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            if request.user.is_authenticated:
                appointment.patient = request.user
            appointment.save()
            messages.success(
                request,
                "Your appointment request has been received! "
                "Our team will contact you shortly to confirm."
            )
            return redirect('appointments:appointment_success')
    else:
        form = AppointmentForm(initial=initial)

    context = {
        'form': form,
        'preselected_service': service_slug,
        'preselected_doctor': doctor_slug,
    }
    return render(request, 'appointments/book_appointment.html', context)


def appointment_success_view(request):
    """Render the appointment confirmation success page."""
    return render(request, 'appointments/appointment_success.html')