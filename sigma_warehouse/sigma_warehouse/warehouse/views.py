from rest_framework import viewsets

from sigma_warehouse.warehouse.models import Item
from sigma_warehouse.warehouse.serializers import ItemSerializer


class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer