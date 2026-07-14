"""
Core app forms.

Reserved for core-level forms such as the homepage Emergency Callback
request form used in the Emergency Dental Banner section.
"""

from django import forms


class EmergencyCallbackForm(forms.Form):
    """Quick callback request form used in the Emergency Dental Banner."""

    full_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Your Full Name',
        })
    )
    phone = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Your Phone Number',
        })
    )