"""
Services app models.

Represents dental services offered by the clinic (Teeth Cleaning,
Dental Implants, Root Canal, Braces, etc.), each with an image,
description, benefits, and a demo price.
"""

from django.db import models


class Service(models.Model):
    """A dental service offered by BrightSmile Dental Care."""

    ICON_CHOICES = [
        ('cleaning', 'Teeth Cleaning'),
        ('implant', 'Dental Implants'),
        ('root_canal', 'Root Canal'),
        ('braces', 'Braces'),
        ('whitening', 'Teeth Whitening'),
        ('cosmetic', 'Cosmetic Dentistry'),
        ('emergency', 'Emergency Care'),
        ('pediatric', 'Pediatric Dentistry'),
        ('surgery', 'Oral Surgery'),
    ]

    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=170, unique=True)
    image = models.ImageField(upload_to='services/')
    icon = models.CharField(max_length=20, choices=ICON_CHOICES, default='cleaning')
    short_description = models.CharField(
        max_length=255,
        help_text="One-line summary shown on service cards."
    )
    full_description = models.TextField(
        help_text="Detailed description shown on the service detail page."
    )
    benefits = models.TextField(
        help_text="One benefit per line. Will be displayed as a bullet list."
    )
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        help_text="Demo price in USD, e.g. 150.00"
    )
    duration_minutes = models.PositiveIntegerField(
        default=30,
        help_text="Typical appointment duration in minutes."
    )

    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'name']
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.name

    def benefit_list(self):
        """Return the benefits field split into a clean list of lines."""
        return [line.strip() for line in self.benefits.splitlines() if line.strip()]

    def formatted_price(self):
        """Return the price formatted as a US dollar string, e.g. '$150'."""
        if self.price == int(self.price):
            return f"${int(self.price)}"
        return f"${self.price}"