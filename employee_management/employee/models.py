import re
from django.db import models
from django.forms import ValidationError
from base.models import BaseModel


def validate_number(value):
    number_pattern = r'^\(\+(\d\d\d)\)\s?(\d{5,})$'
    if not re.match(number_pattern, value):
        raise ValidationError('Enter a valid Rwandan phone number')

class Employee(BaseModel):
    email = models.EmailField(unique=True, null=False, blank=False)
    employeeId = models.CharField(max_length=10, unique=True, blank=False)
    phone_number = models.CharField(max_length=15, blank=False, validators=validate_number)

    # For validating the uniqueness of employee IDs
    def save(self, *args, **kwargs):
        if not self.employeeId:
            last_employee = Employee.objects.all().order_by('id').last()
            if last_employee:
                last_id = int(last_employee.employeeId[3:])
                new_id = last_id + 1
            else:
                new_id = 1
            self.employeeId = f"EMP{new_id:03d}"
        super(Employee, self).save(*args, **kwargs)