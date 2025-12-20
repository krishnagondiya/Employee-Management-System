from django.shortcuts import render, redirect
from .models import Department
from django.contrib.auth.decorators import login_required

@login_required
def department_list(request):
    departments = Department.objects.all()
    return render(request, 'departments/department_list.html', {
        'departments': departments
    })

@login_required
def department_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            Department.objects.create(name=name)
            return redirect('departments:list')

    return render(request, 'departments/department_add.html')
