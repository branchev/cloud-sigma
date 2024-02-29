from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounting/', include('sigma_accounting.accounting.urls', namespace='accounting')),
]
