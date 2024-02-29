from django.contrib import admin
from django.urls import include, path, re_path

from rest_framework import permissions, routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from sigma_warehouse.users.views import CustomAuthToken
from sigma_warehouse.warehouse.views import WarehouseViewSet


schema_view = get_schema_view(
    openapi.Info(
        title="API Gateway Documentation",
        default_version='v1',
        description="API Gateway documentation for Warehouse microservice",
        terms_of_service="https://www.example.com/policies/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)



router = routers.DefaultRouter()
router.register(r"warehouse/items", WarehouseViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),

    # API endpoints documentation
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    # API urls
    path('api-token-auth/', CustomAuthToken.as_view()),
    path('api/', include(router.urls)),
    path('api/buy-tem/', WarehouseViewSet.as_view({'put': 'buy_item'}), name='buy-item'),
]
