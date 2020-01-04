from django.db.models import Q
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.http.response import JsonResponse
from .models import Employee, DEPARTMENT_CHOICES
from .forms import EmployeeForm


class EmployeeListView(generic.ListView):
    template_name = 'employee/list.html'
    model = Employee

    def get_queryset(self):
        q = self.request.GET.get('q', '')
        return Employee.query_by_text(q)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['departments'] = list(map(lambda x: x[0], DEPARTMENT_CHOICES))
        context['q'] = self.request.GET.get('q', '')
        return context


class EmployeeCreateView(generic.CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employee/list.html'
    success_url = reverse_lazy('grabar_employee:list')


class EmployeeMofifyView:
    def post(self, request):
        form = EmployeeForm(request.POST)
        if form.is_valid():
            pass
        return JsonResponse()
