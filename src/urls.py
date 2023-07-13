from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view


schema_view = get_schema_view(
   openapi.Info(
       title="Task Manager",
       default_version='v1',
       contact=openapi.Contact(email="aza@gmail.com"),
   ),
   public=True,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', include('accounts.routes.urls.v1')),
    path('dashboard/', include('courses.routes.urls.v1')),
]
