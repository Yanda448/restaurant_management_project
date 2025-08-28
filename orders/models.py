from django.db import models

# Create your models here.
class SalesReport(models.Model):
    date = models.DateField(unique=True)
    total_orders = models.IntegerField()
    total_sales = models.DecimalField(max_digits=10, decimal_places=2)
    top_item = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.date} - {self.total_sales}"