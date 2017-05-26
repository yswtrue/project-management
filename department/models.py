from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class BaseModel(models.Model):
    '''基类'''
    class Meta:
        abstract = True


class Department(BaseModel):
    '''部门'''
    name = models.CharField(max_length=200)
    description = models.TextField()


class Employee(BaseModel):
    user = models.OneToOneField(
        User, related_name='employee', on_delete=models.CASCADE)
    description = models.TextField()
    department = models.ForeignKey(
        Department,
        related_name='employees'
    )
