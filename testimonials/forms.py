"""
Testimonials app forms.

Provides the form used by patients to add or edit a testimonial.
"""

from django import forms

from .models import Testimonial


class TestimonialForm(forms.ModelForm):
    """Form for creating or editing a patient testimonial."""

    class Meta:
        model = Testimonial
        fields = ['patient_name', 'patient_location', 'rating', 'review_text']
        widgets = {
            'patient_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Name',
            }),
            'patient_location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your City, State',
            }),
            'rating': forms.Select(attrs={
                'class': 'form-control',
            }),
            'review_text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Share your experience with us...',
                'rows': 4,
            }),
        }