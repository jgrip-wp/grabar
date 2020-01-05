from django.urls import path
from .views import *


app_name = 'grabar_partner'
urlpatterns = [
    path('', PartnerListView.as_view(), name='list'),
]
