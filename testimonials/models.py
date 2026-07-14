"""
Testimonials app models.

Handles patient reviews with a 1-5 star rating. Patients can add,
edit, and delete their own reviews; reviews require admin approval
before appearing publicly.
"""

from django.conf import settings
from django.db import models


class Testimonial(models.Model):
    """A patient review/testimonial with a star rating."""

    RATING_CHOICES = [
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    ]

    patient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='testimonials',
    )
    patient_name = models.CharField(
        max_length=150,
        help_text="Display name shown publicly with the review."
    )
    patient_location = models.CharField(
        max_length=100,
        blank=True,
        help_text="e.g. 'New York, USA'"
    )
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES, default=5)
    review_text = models.TextField()

    is_approved = models.BooleanField(
        default=False,
        help_text="Only approved reviews are shown publicly on the site."
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'

    def __str__(self):
        return f"{self.patient_name} - {self.rating} Stars"

    def star_range(self):
        """Return a range object usable in templates to render filled stars."""
        return range(self.rating)

    def empty_star_range(self):
        """Return a range object usable in templates to render empty stars."""
        return range(5 - self.rating)