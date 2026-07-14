"""
URL patterns for the core app.
"""

from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about-us/', views.about_view, name='about'),
    path('faq/', views.faq_view, name='faq'),
    path('gallery/', views.gallery_view, name='gallery'),
    path('pricing/', views.pricing_view, name='pricing'),
    path('privacy-policy/', views.privacy_policy_view, name='privacy_policy'),
    path('terms-and-conditions/', views.terms_conditions_view, name='terms_conditions'),
]