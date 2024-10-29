from django.db import models
from django.contrib.auth.models import User
from base.models import BaseModel


# Create your models here.
class Account(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to='account_images', null=True, editable=True)

    def __str__(self):
        return self.user


class PasswordReset(models.Model):
    email = models.EmailField(max_length=255)
    otp = models.CharField(max_length=10)

    def __str__(self):
        return self.email
    

class ConfirmReset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=10)