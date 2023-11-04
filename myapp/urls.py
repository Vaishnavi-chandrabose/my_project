from django.urls import path
from . import views

from django.shortcuts import get_object_or_404

urlpatterns = [
    path('employee_list/', views.employee_list, name='employee_list'),
    path('add_employee/', views.add_employee, name='add_employee'),
    path('delete_employee/<int:employee_id>/', views.delete_employee, name='delete_employee'),

    path('get_employee/<int:employee_id>/', views.get_employee, name='get_employee'),
    path('update_employee/<int:employee_id>/', views.update_employee, name='update_employee'),
]
