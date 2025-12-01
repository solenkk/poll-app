from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Swagger/OpenAPI configuration
schema_view = get_schema_view(
    openapi.Info(
        title="Poll System API",
        default_version='v1',
        description="API documentation for the Online Poll System",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@pollsystem.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Django Admin
    path('admin/', admin.site.urls),
    
    # Our API endpoints
    path('api/', include('poll_app.urls')),
    
    # Swagger/OpenAPI Documentation
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]