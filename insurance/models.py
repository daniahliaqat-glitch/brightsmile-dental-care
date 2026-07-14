"""
Insurance app models.

Handles insurance partners and the plans they offer, displayed
on the Insurance page alongside logos and accepted plan details.
"""

from django.db import models


class InsurancePartner(models.Model):
    """An insurance company that BrightSmile Dental Care partners with."""

    name = models.CharField(max_length=150)
    logo = models.ImageField(upload_to='insurance/')
    website_url = models.URLField(blank=True)

    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'name']
        verbose_name = 'Insurance Partner'
        verbose_name_plural = 'Insurance Partners'

    def __str__(self):
        return self.name


class AcceptedPlan(models.Model):
    """A specific insurance plan accepted at the clinic, tied to a partner."""

    partner = models.ForeignKey(
        InsurancePartner,
        on_delete=models.CASCADE,
        related_name='plans',
    )
    plan_name = models.CharField(max_length=150)
    coverage_details = models.TextField(
        help_text="Short summary of what this plan covers."
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['partner__name', 'plan_name']
        verbose_name = 'Accepted Plan'
        verbose_name_plural = 'Accepted Plans'

    def __str__(self):
        return f"{self.partner.name} - {self.plan_name}"