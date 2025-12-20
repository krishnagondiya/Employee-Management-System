from django.urls import path
from . import views

app_name = 'departments'

urlpatterns = [
    path('', views.department_list, name='list'),
    path('add/', views.department_add, name='add'),
]
