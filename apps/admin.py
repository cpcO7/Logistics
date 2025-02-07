from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.models import (
    Statistic, CentralBlock, CompanyInfo, Group, Service, Partner,
    PartnersImage, ClientComment, Article, AppliedClient, Companies,
    Question, Answer, Agent, AboutUs, TimeManagement
)

models = [
    Statistic, CentralBlock, CompanyInfo, Group, Service, Partner,
    PartnersImage, ClientComment, Article, AppliedClient, Companies,
    Question, Answer, Agent, TimeManagement
]

for model in models:
    admin.site.register(model, ModelAdmin)


from django.shortcuts import redirect
from django.urls import reverse

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if AboutUs.objects.exists():
            return False
        return True

    def changelist_view(self, request, extra_context=None):
        if AboutUs.objects.exists():
            obj = AboutUs.objects.first()
            return redirect(reverse('admin:apps_aboutus_change', args=[obj.id]))
        return super().changelist_view(request, extra_context)