from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.models import (
    Statistic, Group, Service, Partner,
    PartnerImage, ClientComment, Article, AppliedClient, Companies,
    Question, Agent, AboutUs, TimeManagement, Email, Candidate, Contact
)

models = [
    Statistic, Group, Service, ClientComment, Article, Companies,
    Question, Agent, TimeManagement, Email, Candidate, Contact
]

for model in models:
    admin.site.register(model, ModelAdmin)

from django.shortcuts import redirect
from django.urls import reverse


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('phone_number',)

    class Media:
        js = ("admin/js/phone_mask.js",)

    def has_add_permission(self, request):
        if AboutUs.objects.exists():
            return False
        return True

    def changelist_view(self, request, extra_context=None):
        if AboutUs.objects.exists():
            obj = AboutUs.objects.first()
            return redirect(reverse('admin:apps_aboutus_change', args=[obj.id]))
        return super().changelist_view(request, extra_context)


    fieldsets = (
        ("Main Information", {
            "fields": ("phone_number", "email")
        }),
        ("Social Media", {
            "fields": ("facebook", "twitter", "instagram", "linkedin", "telegram")
        }),
        ("Working Time", {
            "fields": ("work_day", "work_hour_start", "work_hour_end")
        }),
        (
            "Address", {
                "fields": ("address", "search", "location")
            }
        )
    )
@admin.register(AppliedClient)
class AppliedClientAdmin(admin.ModelAdmin):
    list_display = ('phone_number',)

    class Media:
        js = ("admin/js/phone_mask.js",)

class PartnerImageInline(admin.TabularInline):  # Yoki admin.StackedInline
    model = PartnerImage
    extra = 0
    max_num = 3
    min_num = 3


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    inlines = PartnerImageInline,
    def has_add_permission(self, request):
        if Partner.objects.exists():
            return False
        return True

    def changelist_view(self, request, extra_context=None):
        if Partner.objects.exists():
            obj = Partner.objects.first()
            return redirect(reverse('admin:apps_partner_change', args=[obj.id]))
        return super().changelist_view(request, extra_context)