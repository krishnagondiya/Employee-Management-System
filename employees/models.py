from django.db import models
from django.conf import settings

class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    designation = models.CharField(max_length=100, blank=True)
    salary = models.IntegerField(default=0)
    mobile = models.CharField(max_length=20, blank=True)
    dt_join = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return f"{self.name} ({self.user.username})"

class LeaveRequest(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    )
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    from_date = models.DateField()
    to_date = models.DateField()
    reason = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"{self.employee.name} - {self.from_date} to {self.to_date} ({self.status})"

class SalaryRecord(models.Model):
    STATUS_CHOICES = (
        ('Paid', 'Paid'),
        ('Pending', 'Pending'),
    )
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    month = models.CharField(max_length=50)
    amount = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"{self.employee.name} - {self.month} ({self.status})"
