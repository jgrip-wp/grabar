from django.shortcuts import render
from django.views import generic
from django.http.response import JsonResponse
from .models import Employee, DEPARTMENT_CHOICES
from .forms import EmployeeForm


class EmployeeListView(generic.ListView):
    template_name = 'employee/list.html'
    model = Employee

    def get_context_data(self, *, object_list=None, **kwargs):
        kwargs['departments'] = list(map(lambda x: x[0], DEPARTMENT_CHOICES))
        return super().get_context_data(object_list=object_list, **kwargs)


class EmployeeMofifyView:
    def post(self, request):
        form = EmployeeForm(request.POST)
        if form.is_valid():
            pass
        return JsonResponse()
