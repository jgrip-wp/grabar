from django.forms import Form, ModelForm
from .models import Employee


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = (
            'number',
            'name',
            'name_kana',
            'email',
            'department',
            'thumbnail',
        )
