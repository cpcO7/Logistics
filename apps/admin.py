from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.utils.safestring import mark_safe

from apps.models import (
    Statistic, Group, Service, Partner, ClientComment, Article, AppliedClient, Companies,
    Question, Job, AboutUs, TimeManagement, Email, Candidate, Contact, JobCategory, CompanyCategory
)

models = [
    Statistic, Service, ClientComment, Article,
    Question, Job, TimeManagement, Email, Partner, JobCategory, CompanyCategory
]

for model in models:
    admin.site.register(model, ModelAdmin)

from django.shortcuts import redirect
from django.urls import reverse


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('formatted_description', 'image_tag',)

    def formatted_description(self, obj):
        return mark_safe(obj.description)

    formatted_description.short_description = "Description"

    def image_tag(self, obj):
        if obj.image:
            return mark_safe(
                f'<img src="{obj.image.url}" width="30" height="30" style="object-fit: cover; border-radius: 5px;" />')
        return "No Image"

    image_tag.short_description = "Image"


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
    list_display = 'first_name', 'last_name', 'email', 'phone_number'

    class Media:
        js = ("admin/js/phone_mask.js",)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'first_name', 'last_name', 'email', 'phone_number'


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = 'first_name', 'last_name', 'country', 'city'


@admin.register(Companies)
class CompaniesAdmin(admin.ModelAdmin):
    list_display = 'name', 'image_tag', 'clickable_url'

    def image_tag(self, obj):
        if obj.image:
            return mark_safe(
                f'<img src="{obj.image.url}" width="30" height="30" style="object-fit: cover; border-radius: 5px;" />')
        return "No Image"

    def clickable_url(self, obj):
        if obj.url:
            return mark_safe(f'<a href="{obj.url}" target="_blank">{obj.url}</a>')
        return "No URL"
