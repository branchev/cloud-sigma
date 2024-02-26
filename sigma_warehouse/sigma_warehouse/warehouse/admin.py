from django.contrib import admin

from sigma_warehouse.warehouse.models import Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')
    list_per_page = 25


admin.site.register(Item, ItemAdmin)
