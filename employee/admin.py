from django.contrib import admin
from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password', 'name', 'name_kana', 'department')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
    list_display = ('email', 'department', 'name')
    list_filter = ('department', 'is_active')
    ordering = ('department', 'email')
