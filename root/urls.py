from django.conf.urls.static import static
from django.http import HttpResponseNotFound
from django.urls import path, include
from django.contrib import admin
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from root.settings import MEDIA_ROOT, MEDIA_URL, STATIC_URL, STATIC_ROOT, ALLOWED_HOSTS

urlpatterns = [
                  path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
                  path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
                  path('api/v1/', include("apps.urls")),
                  path("ckeditor5/", include('django_ckeditor_5.urls')),
              ] + static(MEDIA_URL, document_root=MEDIA_ROOT) + static(STATIC_URL, document_root=STATIC_ROOT)


def not_found(request):
    return HttpResponseNotFound("Page not found")


if ALLOWED_HOSTS:
    if 'admin.cpco7.online' in ALLOWED_HOSTS:
        urlpatterns.append(path('', admin.site.urls))
