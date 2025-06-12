from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main, name='main'), #get and post req for insert operation
    path('<int:id>/', views.employee_form, name='employee_update'), #get and post req for update operation
    path('delete/<int:id>/', views.employee_delete, name='employee_delete'),
    path('employee/list/', views.employee_list, name='employee_list'), #get and req to retrieve and display all records
    path('employee/', views.employee_form, name="employee_form")

]