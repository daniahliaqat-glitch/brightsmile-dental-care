"""
URL patterns for the appointments app.
"""

from django.urls import path
from . import views

app_name = 'appointments'

urlpatterns = [
    path('book/', views.book_appointment_view, name='book_appointment'),
    path('success/', views.appointment_success_view, name='appointment_success'),
]