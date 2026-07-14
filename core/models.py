"""
Core app models.

Handles content that supports static/informational pages:
Why Choose Us features, Gallery images, and FAQ entries.
"""

from django.db import models


class WhyChooseUsFeature(models.Model):
    """Feature card shown in the 'Why Choose Us' homepage section."""

    ICON_CHOICES = [
        ('tooth', 'Tooth Icon'),
        ('shield', 'Shield Icon'),
        ('clock', 'Clock Icon'),
        ('smile', 'Smile Icon'),
        ('heart', 'Heart Icon'),
        ('star', 'Star Icon'),
    ]

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    icon = models.CharField(max_length=20, choices=ICON_CHOICES, default='tooth')
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']
        verbose_name = 'Why Choose Us Feature'
        verbose_name_plural = 'Why Choose Us Features'

    def __str__(self):
        return self.title


class ClinicStat(models.Model):
    """Numeric statistic shown in floating stat cards (e.g. '15+ Years Experience')."""

    label = models.CharField(max_length=100)
    value = models.CharField(max_length=20, help_text="e.g. '15+', '2500+', '98%'")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']
        verbose_name = 'Clinic Statistic'
        verbose_name_plural = 'Clinic Statistics'

    def __str__(self):
        return f"{self.value} {self.label}"


class GalleryImage(models.Model):
    """Image used in the clinic gallery page."""

    CATEGORY_CHOICES = [
        ('clinic', 'Clinic'),
        ('team', 'Team'),
        ('procedures', 'Procedures'),
        ('happy_patients', 'Happy Patients'),
    ]

    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='gallery/')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='clinic')
    is_active = models.BooleanField(default=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-uploaded_at']
        verbose_name = 'Gallery Image'
        verbose_name_plural = 'Gallery Images'

    def __str__(self):
        return self.title


class FAQ(models.Model):
    """Frequently asked question entry, usable on the FAQ page and Insurance page."""

    CATEGORY_CHOICES = [
        ('general', 'General'),
        ('appointments', 'Appointments'),
        ('insurance', 'Insurance'),
        ('billing', 'Billing'),
    ]

    question = models.CharField(max_length=255)
    answer = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='general')
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'

    def __str__(self):
        return self.question