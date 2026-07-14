"""
URL patterns for the testimonials app.
"""

from django.urls import path
from . import views

app_name = 'testimonials'

urlpatterns = [
    path('', views.testimonial_list_view, name='testimonial_list'),
    path('add/', views.testimonial_add_view, name='testimonial_add'),
    path('<int:pk>/edit/', views.testimonial_edit_view, name='testimonial_edit'),
    path('<int:pk>/delete/', views.testimonial_delete_view, name='testimonial_delete'),
]