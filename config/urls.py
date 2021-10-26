from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/signals/', include('signals.urls')),
    path('api/v2/signals/', include('signals_v2.urls')),
    path('api/v3/signals/', include('signals_v3.urls')),
]
