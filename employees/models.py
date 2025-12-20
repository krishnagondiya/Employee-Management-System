from django.db import models
from accounts.models import User
from departments.models import Department

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    designation = models.CharField(max_length=100)
    salary = models.IntegerField()
    mobile = models.CharField(max_length=15)
    date_joined = models.DateField()
    address = models.TextField()
    email = models.EmailField(null=True, blank=True)
    role = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name