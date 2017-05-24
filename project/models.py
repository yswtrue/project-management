from django.db import models
from department.models import BaseModel
from department.models import Employee

# Create your models here.


class Project(BaseModel):
    # 项目名
    name = models.CharField(max_length=200)


class List(BaseModel):
    # 列表名
    name = models.CharField(max_length=200)
    # 关联的项目
    project = models.ForeignKey(
        Project,
        default=None,
        null=True,
        related_name='lists'
    )


class Tag(BaseModel):
    # 标签名
    name = models.CharField(max_length=200)
    # 排序
    sort = models.IntegerField(
        default=0
    )
    # 属于哪个项目
    project = models.ForeignKey(
        Project,
        default=None,
        null=True
    )


class Task(BaseModel):
    # 任务名
    name = models.CharField(max_length=200)
    # 任务起始日期
    start_date = models.DateField(null=True)
    # 任务结束日期
    end_date = models.DateField(null=True)
    # 任务状态
    status = models.BooleanField(
        default=False
    )
    # 任务内容
    content = models.TextField()
    # 任务关联到的列表
    list = models.ForeignKey(
        List,
        default=None,
        null=True,
        related_name='tasks'
    )
    # 任务关联到的标签
    tags = models.ManyToManyField(
        Tag,
        related_name='tasks'
    )
    # 任务发起者
    creator = models.ForeignKey(
        Employee,
        related_name='created_tasks',
        default=None,
        null=True
    )
    # 任务的参与者
    partners = models.ManyToManyField(
        Employee,
        related_name='tasks'
    )
    # 父级任务
    parent = models.ForeignKey(
        'self',
        related_name='children',
        default=None,
        null=True
    )


class Comment(BaseModel):
    # 评论内容
    content = models.TextField()
    # 关联到的任务
    task = models.ForeignKey(
        Task,
        default=None,
        null=True,
        related_name='comments'
    )
