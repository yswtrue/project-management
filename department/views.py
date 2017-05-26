from django.db import transaction
from django.contrib.auth.models import User
from rest_framework import viewsets
from . import serializers
from . import models


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = models.Department.objects.all()
    serializer_class = serializers.DepartmentSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all()
    # queryset = User.objects.all()
    serializer_class = serializers.EmployeeSerializer

    def perform_create(self, serializer):
        user = User.objects.create_user(self.request.user)
        serializer.save(user=user)
