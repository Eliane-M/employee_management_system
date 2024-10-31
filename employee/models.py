import re
from django.db import models
from django.forms import ValidationError
from base.models import BaseModel
from django.contrib.auth.models import User
from django.utils import timezone


def validate_number(value):
    number_pattern = r'^\(\+(\d\d\d)\)\s?(\d{5,})$'
    if not re.match(number_pattern, value):
        raise ValidationError('Enter a valid Rwandan phone number')
    
def validate_email(value):
    email_pattern = r'^(\S*)@gmail.com$'
    if re.match(email_pattern, value):
        raise ValidationError('Management emails cannot have Gmail adresses.')

class Employee(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True, null=False, blank=False)
    employeeId = models.CharField(max_length=10, unique=True, blank=False)
    phone_number = models.CharField(max_length=15, blank=False, validators=[validate_number])

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

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    check_in_time = models.DateTimeField(null=True, blank=True)
    check_out_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Attendance record for {self.employee.name} on {self.check_in_time.date()}"

class Management(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True, blank=False, validators=[validate_email])
    phone_number = models.CharField(max_length=15, blank=False, validators=[validate_number])
    slug = models.SlugField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (self.user.username)