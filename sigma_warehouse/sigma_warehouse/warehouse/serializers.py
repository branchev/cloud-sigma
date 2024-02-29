from rest_framework import serializers

from sigma_warehouse.warehouse.models import Item


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ['pk', 'quantity']

    def validate_quantity(self, *kwargs):
        value, *_ = kwargs
        if value > self.instance.quantity:
            raise serializers.ValidationError("Insufficient quantity")