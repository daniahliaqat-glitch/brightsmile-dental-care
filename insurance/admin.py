"""
Admin configuration for the insurance app.
"""

from django.contrib import admin
from .models import InsurancePartner, AcceptedPlan


class AcceptedPlanInline(admin.TabularInline):
    model = AcceptedPlan
    extra = 1


@admin.register(InsurancePartner)
class InsurancePartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    search_fields = ('name',)
    inlines = [AcceptedPlanInline]


@admin.register(AcceptedPlan)
class AcceptedPlanAdmin(admin.ModelAdmin):
    list_display = ('plan_name', 'partner', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('is_active', 'partner')
    search_fields = ('plan_name',)