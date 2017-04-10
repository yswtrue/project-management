from django.db import models

# Create your models here.


class BaseModel(models.Model):
    '''基类'''
    class Meta:
        abstract = True


class Department(BaseModel):
    '''部门'''
    name = models.CharField(max_length=200)
    description = models.TextField()


class User(BaseModel):
    user_name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    nick_name = models.CharField(max_length=200)
    description = models.TextField()
    department = models.ForeignKey(
        Department
    )
