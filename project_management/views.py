from django.shortcuts import render
from django.views.decorators.http import require_http_methods, require_POST
from django.db import transaction
from django.http import JsonResponse
from django.contrib.auth.models import User
from department.models import Employee, Department
from project_management.common import ajax_return, models_to_dict
from django.core import serializers
import json


def index(request):
    return JsonResponse([], safe=False)
