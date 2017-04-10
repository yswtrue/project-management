from django.db import models
from department.models import BaseModel
from department.models import Employee

# Create your models here.


class Project(BaseModel):
    name = models.CharField(max_length=200)


class List(BaseModel):
    name = models.CharField(max_length=200)


class Tag(BaseModel):
    name = models.CharField(max_length=200)
    sort = models.IntegerField(
        default=0
    )
    project = models.ForeignKey(
        List
    )


class Task(BaseModel):
    name = models.CharField(max_length=200)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    status = models.BooleanField(
        default=False
    )
    content = models.TextField()
    list = models.ManyToManyField(
        List
    )
    tag = models.ManyToManyField(
        Tag
    )
    creator = models.ForeignKey(
        Employee,
        related_name='created_tasks'
    )
    partners = models.ManyToManyField(
        Employee,
        related_name='tasks'
    )
    parent = models.ForeignKey(
        'self',
        related_name='children',
        default=None,
        null=True
    )


class Comment(BaseModel):
    content = models.TextField()
    task = models.ForeignKey(
        Task,
    )
