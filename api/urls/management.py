from django.urls import path
from api.views.management.employee_management import *


urlpatterns = [
    path('employee_list/', employee_list, name='get_employees'),
    path('get_employees/', get_employee, name='get_employees'),
    path('add_new_employee/', add_new_employee, name='add_new_employee'),
    path('update_employee/', update_employee, name='update_employee'),
    path('delete_employee/', delete_employee, name='delete')
]