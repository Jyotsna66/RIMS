from django.db import models
from datetime import datetime

# Create your models here.
class SalesEntry(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField()
    phonepe_upi = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    card_pmt = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    zomato = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    swiggy = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    bms = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    cash = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    expenditure = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    total_sale = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def save(self, *args, **kwargs):
        # Calculate total_sale by summing up all payment methods and subtracting expenditure
        self.total_sale = (
            self.phonepe_upi + self.card_pmt + self.zomato +
            self.swiggy + self.bms + self.cash - self.expenditure
        )
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Sales Entry {self.id} on {self.date}"
    

    
class DailyPurchase(models.Model):
    date = models.DateField(default=datetime.today())
    item_type = models.CharField(max_length=100)
    item_name = models.CharField(max_length=255, default='Unknown Item')
    unit = models.CharField(max_length=20)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    tax = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        self.total_price = (self.quantity * self.price_per_unit) + self.tax
        super().save(*args, **kwargs)


class StockRequisition(models.Model):
    date = models.DateField()
    item_type = models.CharField(max_length=255)
    item_name = models.CharField(max_length=255)
    unit = models.CharField(max_length=100)
    closing = models.FloatField()
    required = models.FloatField()
    delivered = models.FloatField()

    def __str__(self):
        return f"{self.item_name} ({self.date})"
