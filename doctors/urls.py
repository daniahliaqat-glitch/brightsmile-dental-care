"""
URL patterns for the doctors app.
"""

from django.urls import path
from . import views

app_name = 'doctors'

urlpatterns = [
    path('', views.doctor_list_view, name='doctor_list'),
    path('<slug:slug>/', views.doctor_detail_view, name='doctor_detail'),
]