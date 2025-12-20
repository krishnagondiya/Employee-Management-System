from django.urls import path
from . import views

app_name = 'leaves'

urlpatterns = [
    path('', views.leave_list, name='list'),
    path('add/', views.leave_add, name='add'),
]
