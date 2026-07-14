"""
Newsletter app views.

Handles newsletter subscription form submissions, which are received
via POST from the newsletter bar present on multiple pages.
"""

from django.contrib import messages
from django.shortcuts import redirect

from .forms import NewsletterSubscriberForm


def newsletter_subscribe_view(request):
    """Handle a newsletter subscription form submission and redirect back."""
    if request.method == 'POST':
        form = NewsletterSubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have successfully subscribed to our newsletter!")
        else:
            messages.error(request, "Please enter a valid email address.")

    next_url = request.POST.get('next') or request.META.get('HTTP_REFERER') or '/'
    return redirect(next_url)