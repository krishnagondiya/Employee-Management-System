from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.home, name='home'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
]
