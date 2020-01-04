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

    def test_search_employee(self):
        """
        Employee.query_by_text() returns Employee corresponding to the text
        """
        text = '神'
        x = Employee.query_by_text(text)
        self.assertEqual(1, len(x))
        self.assertTrue(all(map(lambda x: text in x.name, x)))

        text = 'ほんだ'
        x = Employee.query_by_text(text)
        self.assertEqual(1, len(x))
        self.assertTrue(all(map(lambda x: text in x.name_kana, x)))

        text = 'ushiro'
        x = Employee.query_by_text(text)
        self.assertEqual(1, len(x))
        self.assertTrue(all(map(lambda x: text in x.email, x)))