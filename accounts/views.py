"""
Accounts app views.

Handles patient registration, login, logout, profile viewing,
profile editing, and a UI-only forgot password page.
"""

from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import (
    PatientRegisterForm,
    ProfileUpdateForm,
    PatientProfileUpdateForm,
    ForgotPasswordForm,
)


def register_view(request):
    """Handle new patient registration."""
    if request.user.is_authenticated:
        return redirect('dashboard:patient_dashboard')

    if request.method == 'POST':
        form = PatientRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Welcome to BrightSmile Dental Care, {user.first_name}!")
            return redirect('dashboard:patient_dashboard')
    else:
        form = PatientRegisterForm()

    return render(request, 'accounts/register.html', {'form': form})


class PatientLoginView(LoginView):
    """Login view for patients using the custom login template."""

    template_name = 'accounts/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('dashboard:patient_dashboard')

    def form_valid(self, form):
        messages.success(self.request, "You have successfully logged in.")
        return super().form_valid(form)


def logout_view(request):
    """Log the current user out and redirect to the homepage."""
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('core:home')


def forgot_password_view(request):
    """Render a UI-only forgot password request page."""
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            messages.success(
                request,
                "If an account exists with that email, password reset instructions "
                "have been sent."
            )
            return redirect('accounts:login')
    else:
        form = ForgotPasswordForm()

    return render(request, 'accounts/forgot_password.html', {'form': form})


@login_required
def profile_view(request):
    """Render the current patient's profile page."""
    return render(request, 'accounts/profile.html', {
        'patient_profile': request.user.patient_profile,
    })


@login_required
def edit_profile_view(request):
    """Handle editing the current patient's profile information."""
    if request.method == 'POST':
        user_form = ProfileUpdateForm(request.POST, instance=request.user)
        profile_form = PatientProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.patient_profile
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Your profile has been updated successfully.")
            return redirect('accounts:profile')
    else:
        user_form = ProfileUpdateForm(instance=request.user)
        profile_form = PatientProfileUpdateForm(instance=request.user.patient_profile)

    return render(request, 'accounts/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })