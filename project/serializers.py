from rest_framework import serializers
from project import models


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    tags = TagSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = models.Task
        fields = '__all__'


class ListSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = models.List
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    lists = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True
    )

    class Meta:
        model = models.Project
        fields = '__all__'
        depth = 2


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = '__all__'
