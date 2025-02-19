from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.models import (
    Statistic, Group, Service, Partner, ClientComment, Article, AppliedClient, Companies,
    Question, Job, AboutUs, TimeManagement, Email, Candidate, Contact, JobCategory, CompanyCategory
)

models = [
    Statistic, Group, Service, ClientComment, Article, Companies,
    Question, Job, TimeManagement, Email, Candidate, Contact, Partner, JobCategory, CompanyCategory
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

    def save_model(self, request, obj, form, change):
        obj.search = None
        obj.search1 = None
        obj.search2 = None
        super().save_model(request, obj, form, change)

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
            "Main Address", {
                "fields": ("address", "search", "location")
            }
        ),
        (
            "Address 1", {
                "fields": ("address1", "search1", "location1")
            }
        ),
        (
            "Address 2", {
                "fields": ("address2", "search2", "location2")
            }
        )
    )
@admin.register(AppliedClient)
class AppliedClientAdmin(admin.ModelAdmin):
    list_display = ('phone_number',)

    class Media:
        js = ("admin/js/phone_mask.js",)
