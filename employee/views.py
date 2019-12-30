from django.shortcuts import render
from django.views import generic
from .models import Employee


class EmployeeListView(generic.ListView):
    template_name = 'employee/list.html'
    model = Employee
