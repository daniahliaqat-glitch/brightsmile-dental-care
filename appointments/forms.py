"""
Appointments app forms.

Provides the appointment booking form used on the Book Appointment page.
"""

from django import forms

from .models import Appointment
from doctors.models import Doctor
from services.models import Service


class AppointmentForm(forms.ModelForm):
    """Form for booking a new appointment."""

    class Meta:
        model = Appointment
        fields = [
            'full_name',
            'phone',
            'email',
            'appointment_date',
            'appointment_time',
            'doctor',
            'service',
            'message',
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your full name',
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your phone',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email',
            }),
            'appointment_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
            'appointment_time': forms.TimeInput(attrs={
                'class': 'form-control',
                'type': 'time',
            }),
            'doctor': forms.Select(attrs={
                'class': 'form-control',
            }),
            'service': forms.Select(attrs={
                'class': 'form-control',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Message (optional)',
                'rows': 4,
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['doctor'].queryset = Doctor.objects.filter(is_active=True)
        self.fields['service'].queryset = Service.objects.filter(is_active=True)
        self.fields['message'].required = False