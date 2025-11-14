from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignupForm, LoginForm
from .models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse

def index(request):
    if request.user.is_authenticated:
        if request.user.role == 'Admin':
            return redirect('admin_dashboard')
        return redirect('employee_dashboard')
    return redirect('login')

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, 'Account created successfully. Please login.')
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.role == 'Admin':
                return redirect('admin_dashboard')
            return redirect('employee_dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def admin_dashboard(request):
    if request.user.role != 'Admin':
        messages.error(request, 'Access denied.')
        return redirect('employee_dashboard')
    from employees.models import Employee, Department, LeaveRequest
    total_employees = Employee.objects.count()
    total_departments = Department.objects.count()
    pending_leaves = LeaveRequest.objects.filter(status='Pending').count()
    context = {
        'total_employees': total_employees,
        'total_departments': total_departments,
        'pending_leaves': pending_leaves
    }
    return render(request, 'accounts/admin_dashboard.html', context)

@login_required
def employee_dashboard(request):
    if request.user.role == 'Admin':
        return redirect('admin_dashboard')
    from employees.models import Employee
    employee = None
    try:
        employee = Employee.objects.get(user=request.user)
    except Employee.DoesNotExist:
        employee = None
    return render(request, 'accounts/employee_dashboard.html', {'employee': employee})