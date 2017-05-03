from django.shortcuts import render
from django.views.decorators.http import require_http_methods, require_POST
from django.db import transaction
from django.http import JsonResponse
from django.contrib.auth.models import User
from department.models import Employee, Department
from project_management.common import ajax_return, models_to_dict
from django.core import serializers
import json
# Create your views here.


@ajax_return
@require_POST
@transaction.atomic
def sign_up(request):
    post = json.loads(request.body)
    user = User.objects.create_user(
        username=post.get('username'), password=post.get('password')
    )
    department = Department.objects.get(
        id=post.get('department_id')
    )
    employee = Employee.objects.create(
        user=user,
        department=department
    )
    return user


@ajax_return
def get_departments(request):
    departments = Department.objects.all()
    return departments


@ajax_return
def get_users(request):
    users = User.objects.all()
    return users
