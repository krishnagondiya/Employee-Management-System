from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Salary
from employees.models import Employee

@login_required
def salary_list(request):
    salaries = Salary.objects.select_related('employee').all()
    return render(request, 'salary/salary_list.html', {
        'salaries': salaries
    })

@login_required
def salary_add(request):
    if request.method == 'POST':
        employee_id = request.POST.get('employee')
        amount = request.POST.get('amount')

        if employee_id and amount:
            employee = Employee.objects.get(id=employee_id)  # fetch actual Employee object
            Salary.objects.create(
                employee=employee,
                amount=amount,
                month="December",   # you can add a field in the form for month
                paid_on="2025-12-20"  # or use date.today()
            )
            return redirect('salary:list')

    employees = Employee.objects.all()
    return render(request, 'salary/salary_add.html', {
        'employees': employees
    })
