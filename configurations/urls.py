from django.contrib import admin
from django.urls import path,include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
schema_view = get_schema_view(
    openapi.Info(
        title="ToDo Woo API",
        description='Todo Projects',
        default_version='v1',
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="adhamchoriyev234@gmail.com"),
        license=openapi.License(name='Todo Projects'),

    ),
    public = True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('api.urls')),

    path('api-auth/', include('rest_framework.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('allauth/', include('allauth.urls')),
    path('swagger/', schema_view.with_ui(
        'swagger', cache_timeout=0),
        name='schema-swagger-ui'),
    path('redoc/',schema_view.with_ui(
        'redoc', cache_timeout=0),
         name='schema-redoc'),
]