"""
Doctors app models.

Represents dentists/doctors displayed on the 'Our Dentists' page,
including their specialization, experience, education, and working hours.
"""

from django.db import models


class Doctor(models.Model):
    """A dentist working at BrightSmile Dental Care."""

    full_name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=170, unique=True)
    photo = models.ImageField(upload_to='doctors/')
    specialization = models.CharField(max_length=150)
    years_of_experience = models.PositiveIntegerField(default=0)
    education = models.CharField(
        max_length=255,
        help_text="e.g. 'DDS, Harvard School of Dental Medicine'"
    )
    languages = models.CharField(
        max_length=255,
        help_text="Comma-separated, e.g. 'English, Spanish'"
    )
    biography = models.TextField()
    working_hours = models.CharField(
        max_length=255,
        help_text="e.g. 'Mon - Fri: 9:00 AM - 5:00 PM'"
    )

    facebook_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)

    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'full_name']
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'

    def __str__(self):
        return f"Dr. {self.full_name}"

    def language_list(self):
        """Return the languages field split into a clean list."""
        return [lang.strip() for lang in self.languages.split(',') if lang.strip()]