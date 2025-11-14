from django.contrib import admin
from .models import Department, Employee, LeaveRequest, SalaryRecord

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user', 'department', 'designation', 'salary')

@admin.register(LeaveRequest)
class LeaveAdmin(admin.ModelAdmin):
    list_display = ('id', 'employee', 'from_date', 'to_date', 'status')

@admin.register(SalaryRecord)
class SalaryRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'employee', 'month', 'amount', 'status')
