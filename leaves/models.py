from django.db import models
from employees.models import Employee

class LeaveRequest(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    )

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=50)
    from_date = models.DateField()
    to_date = models.DateField()
    reason = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    applied_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.employee.name} - {self.leave_type}"
