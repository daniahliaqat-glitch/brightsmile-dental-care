"""
URL patterns for the contact_us app.
"""

from django.urls import path
from . import views

app_name = 'contact_us'

urlpatterns = [
    path('', views.contact_view, name='contact'),
]