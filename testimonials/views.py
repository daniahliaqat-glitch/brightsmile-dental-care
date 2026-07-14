"""
Testimonials app views.

Handles listing approved testimonials, and letting logged-in patients
add, edit, and delete their own reviews.
"""

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import Testimonial
from .forms import TestimonialForm


def testimonial_list_view(request):
    """Render the public testimonials page showing approved reviews."""
    context = {
        'testimonials': Testimonial.objects.filter(is_approved=True),
    }
    return render(request, 'testimonials/testimonial_list.html', context)


@login_required
def testimonial_add_view(request):
    """Allow a logged-in patient to submit a new testimonial."""
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.patient = request.user
            testimonial.is_approved = False
            testimonial.save()
            messages.success(
                request,
                "Thank you for your review! It will appear publicly after approval."
            )
            return redirect('testimonials:testimonial_list')
    else:
        form = TestimonialForm()

    return render(request, 'testimonials/testimonial_list.html', {
        'form': form,
        'testimonials': Testimonial.objects.filter(is_approved=True),
    })


@login_required
def testimonial_edit_view(request, pk):
    """Allow a patient to edit their own testimonial."""
    testimonial = get_object_or_404(Testimonial, pk=pk, patient=request.user)

    if request.method == 'POST':
        form = TestimonialForm(request.POST, instance=testimonial)
        if form.is_valid():
            updated = form.save(commit=False)
            updated.is_approved = False
            updated.save()
            messages.success(request, "Your review has been updated and is pending re-approval.")
            return redirect('testimonials:testimonial_list')
    else:
        form = TestimonialForm(instance=testimonial)

    return render(request, 'testimonials/testimonial_list.html', {
        'form': form,
        'editing_testimonial': testimonial,
        'testimonials': Testimonial.objects.filter(is_approved=True),
    })


@login_required
def testimonial_delete_view(request, pk):
    """Allow a patient to delete their own testimonial."""
    testimonial = get_object_or_404(Testimonial, pk=pk, patient=request.user)
    testimonial.delete()
    messages.success(request, "Your review has been deleted.")
    return redirect('testimonials:testimonial_list')