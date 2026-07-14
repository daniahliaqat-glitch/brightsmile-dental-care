"""
Newsletter app forms.

Provides the email subscription form used in the newsletter bar.
"""

from django import forms

from .models import NewsletterSubscriber


class NewsletterSubscriberForm(forms.ModelForm):
    """Form for subscribing an email address to the newsletter."""

    class Meta:
        model = NewsletterSubscriber
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email address',
            }),
        }