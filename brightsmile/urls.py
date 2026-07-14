"""
URL configuration for the BrightSmile Dental Care project.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('core.urls', namespace='core')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('doctors/', include('doctors.urls', namespace='doctors')),
    path('services/', include('services.urls', namespace='services')),
    path('appointments/', include('appointments.urls', namespace='appointments')),
    path('testimonials/', include('testimonials.urls', namespace='testimonials')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('insurance/', include('insurance.urls', namespace='insurance')),
    path('contact/', include('contact_us.urls', namespace='contact_us')),
    path('newsletter/', include('newsletter.urls', namespace='newsletter')),
    path('dashboard/', include('dashboard.urls', namespace='dashboard')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])

# Custom error handlers
handler404 = 'core.views.custom_404_view'