from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import LeaveRequest
from employees.models import Employee

@login_required
def leave_list(request):
    leaves = LeaveRequest.objects.all()
    return render(request, 'leaves/leave_list.html', {
        'leaves': leaves
    })

from employees.models import Employee

@login_required
def leave_add(request):
    if request.method == 'POST':
        employee_id = request.POST.get('employee')
        reason = request.POST.get('reason')
        if employee_id and reason:
            employee = Employee.objects.get(id=employee_id)
            LeaveRequest.objects.create(
                employee=employee,
                reason=reason,
                leave_type="Casual",   # add proper field in form
                from_date="2025-12-21",
                to_date="2025-12-22"
            )
            return redirect('leaves:list')

    employees = Employee.objects.all()
    return render(request, 'leaves/leave_add.html', {
        'employees': employees
    })
