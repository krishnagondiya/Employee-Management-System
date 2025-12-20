from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Employee
from departments.models import Department


@login_required
def employee_list(request):
    employees = Employee.objects.select_related('department').all()
    return render(request, 'employees/list.html', {
        'employees': employees
    })


@login_required
def employee_add(request):
    departments = Department.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        department_id = request.POST.get('department')
        salary = request.POST.get('salary')
        date_joined = request.POST.get('date_joined')
        role = request.POST.get('role')

        department = Department.objects.get(id=department_id)

        Employee.objects.create(
            name=name,
            email=email,
            department=department,
            salary=salary,
            date_joined=date_joined,
            role=role
        )
        return redirect('employees:list')

    return render(request, 'employees/form.html', {
        'departments': departments
    })
