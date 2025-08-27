from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Manager', 'Manager'),
        ('Cashier', 'Cashier'),
        ('Waiter', 'Waiter'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Waiter')

    def __str__(self):
        return f"{self.username} ({self.role})"


