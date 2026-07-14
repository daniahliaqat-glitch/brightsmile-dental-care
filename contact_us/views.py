"""
Contact Us app views.

Handles the public Contact page, including form submission and
storing messages in the database.
"""

from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import ContactMessageForm


def contact_view(request):
    """Render the Contact page and handle contact form submissions."""
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Thank you for reaching out! Our team will get back to you shortly."
            )
            return redirect('contact_us:contact')
    else:
        form = ContactMessageForm()

    context = {
        'form': form,
    }
    return render(request, 'contact_us/contact.html', context)