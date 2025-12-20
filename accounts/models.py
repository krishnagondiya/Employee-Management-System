from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Employee', 'Employee'),
    )
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='Employee')

    def __str__(self):
        return f"{self.username} ({self.role})"