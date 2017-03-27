from django.db import models

# Create your models here.


class Employee(models.Model):
    id = models.IntegerField
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    phone = models.CharField(max_length=40)
    department = models.CharField(max_length=40)
