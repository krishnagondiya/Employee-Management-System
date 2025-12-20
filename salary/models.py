from django.db import models
from employees.models import Employee

class Salary(models.Model):
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name='salary_records'
    )
    month = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_on = models.DateField()

    def __str__(self):
        return f"{self.employee.name} - {self.month}"
