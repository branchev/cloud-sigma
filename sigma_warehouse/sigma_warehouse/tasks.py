from celery import shared_task

from sigma_warehouse.warehouse.models import Item, ItemHistory


@shared_task(name="save_data_to_db")
def save_data_to_db(item_id, quantity):
    item = Item.objects.get(pk=item_id)
    item.quantity = item.quantity - quantity
    item.save()

    ItemHistory.objects.create(item_id=item_id, quantity=quantity)