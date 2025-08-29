from django.db import models

# Create your models here.
class SalesReport(models.Model):
    date = models.DateField(unique=True)
    total_orders = models.IntegerField()
    total_sales = models.DecimalField(max_digits=10, decimal_places=2)
    top_item = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.date} - {self.total_sales}"

class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Preparing', 'Preparing'),
        ('Ready', 'Ready'),
        ('Served', 'Served'),
    ]

    customer_name = models.CharField(max_length=100)
    items = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def can_update_to(self, new_status):
        workflow = {
            'Pending': ['Preparing'],
            'Preparing': ['Ready'],
            'Ready': ['Served'],
            'Served': [],
        }
        return new_status in workflow[self.status]
    
    def __str__(self):
        return f"Order {self.id} - {self.customer_name} ({self.status})"