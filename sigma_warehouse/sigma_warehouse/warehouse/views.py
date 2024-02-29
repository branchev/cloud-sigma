from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from drf_yasg import openapi
from drf_spectacular.utils import extend_schema

from sigma_warehouse.warehouse.models import Item
from sigma_warehouse.warehouse.serializers import ItemSerializer
from sigma_warehouse.warehouse.tasks import save_data_to_db


class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    
    def buy_item(self, request, *args, **kwargs):
        pk=request.data.get('pk')
        item = get_object_or_404(Item, pk=request.data.get('pk'))
        serializer = self.serializer_class(item, data=request.data)
        serializer.is_valid(raise_exception=True)
        save_data_to_db.delay(item.id, request.data.get('quantity'))
        return Response(serializer.data)
    
    # Define custom swagger_schema_fields for buy_item method
    buy_item.swagger_schema_fields = {
        'manual_parameters': [
            openapi.Parameter(
                name='pk',
                in_=openapi.IN_PATH,
                type=openapi.TYPE_INTEGER,
                required=True,
                description='A unique integer value identifying the item.'
            ),
        ],
    }

    @extend_schema(
        parameters=[
            openapi.Parameter(
                name='pk',
                in_=openapi.IN_PATH,
                type=openapi.TYPE_INTEGER,
                required=True,
                description='A unique integer value identifying the item.'
            ),
        ],
        responses={200: ItemSerializer}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)   