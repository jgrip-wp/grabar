from django.shortcuts import render
from django.views.generic import ListView
from .models import Partner


class PartnerListView(ListView):
    model = Partner
    template_name = 'partner/list.html'
