from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # AUTH
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),

    # APPS
    path('', include('accounts.urls')),
    path('employees/', include('employees.urls')),
    path('departments/', include('departments.urls')),
    path('leaves/', include('leaves.urls')),
    path('salary/', include('salary.urls')),
]
