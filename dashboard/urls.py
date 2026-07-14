"""
URL patterns for the dashboard app.
"""

from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('patient/', views.patient_dashboard_view, name='patient_dashboard'),
    path('admin-panel/', views.admin_dashboard_view, name='admin_dashboard'),
]