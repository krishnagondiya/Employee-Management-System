from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.http import require_POST
from employees.models import Employee
from departments.models import Department
from leaves.models import LeaveRequest


def home(request):
    if request.user.is_authenticated:
        return redirect('admin_dashboard')
    return redirect('login')


@login_required
def admin_dashboard(request):
    context = {
        'employee_count': Employee.objects.count(),
        'department_count': Department.objects.count(),
        'pending_leaves': LeaveRequest.objects.filter(status='Pending').count(),
    }
    return render(request, 'accounts/admin_dashboard.html', context)


@require_POST
def logout_view(request):
    logout(request)
    return redirect('login')
