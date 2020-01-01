from django.test import TestCase
from .models import Employee

class EmployeeTests(TestCase):
    fixtures = ['employee.json']
    def test_create_employee(self):
        """
        Employee.objects.create_user() creates Employee with given email and password
        """
        employee_list = set(Employee.objects.all())
        email = 'testuser@example.com'
        password = 'ThisIsTest'
        Employee.objects.create_user(email, password)
        employee_list_diff = list(set(Employee.objects.all()) - employee_list)
        self.assertEqual(1, len(employee_list_diff))
        user = employee_list_diff[0]
        self.assertEqual(email, user.email, 'created Employee\'s email should be given one.')
        self.assertNotEqual(password, user.password, 'created Employee\'s password should be hashed.')
        self.assertTrue(user.check_password(password), 'created Employee\'s password should be given one.')
