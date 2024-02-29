from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} - {self.quantity}"

class ItemHistory(models.Model):
    item = models.ForeignKey(Item, related_name='history', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
