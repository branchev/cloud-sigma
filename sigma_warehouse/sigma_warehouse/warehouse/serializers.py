from rest_framework import serializers

from sigma_warehouse.warehouse.models import Item


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = "__all__"