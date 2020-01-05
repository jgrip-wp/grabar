from django.db.models import Q
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.http.response import HttpResponse, HttpResponseBadRequest
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


@require_POST
def create_employee(request):
    form = EmployeeForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return HttpResponse()
    return HttpResponseBadRequest(reason='malformed request')


@require_POST
def update_employee(request, id):
    instance = Employee.objects.get(pk=id)
    form = EmployeeForm(data=request.POST, files=request.FILES, instance=instance)
    if form.is_valid():
        form.save()
        return HttpResponse()
    return HttpResponseBadRequest(reason='malformed request')
