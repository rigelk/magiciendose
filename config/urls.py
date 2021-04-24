from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('pages.urls')),
    path('api/', include('api_urls')),
    path('openapi', get_schema_view(
        title="MagicienDose",
        description="API for MagicienDose",
        version="1.0.0"
    ), name='openapi-schema'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
] + urlpatterns
