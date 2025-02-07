from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from root.settings import MEDIA_ROOT, MEDIA_URL, STATIC_URL, STATIC_ROOT

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
                  path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
                  path('api/v1/', include("apps.urls")),
              ] + static(MEDIA_URL, document_root=MEDIA_ROOT) + static(STATIC_URL, document_root=STATIC_ROOT)
