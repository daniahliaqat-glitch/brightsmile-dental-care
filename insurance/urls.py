"""
URL patterns for the insurance app.
"""

from django.urls import path
from . import views

app_name = 'insurance'

urlpatterns = [
    path('', views.insurance_view, name='insurance'),
]