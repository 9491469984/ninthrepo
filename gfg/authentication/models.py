from django.db import models

# Create your models here.
class Emp(models.Model):
    Emp_name=models.CharField(max_length=100)
    Emp_email=models.CharField(max_length=100)
    Emp_password=models.CharField(max_length=100)