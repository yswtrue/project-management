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


class TaskField(serializers.RelatedField):
    def to_representation(self, value):
        return {'id': value.id, 'name': value.name}


class ListSerializer(serializers.ModelSerializer):
    tasks = TaskField(
        many=True,
        read_only=True
    )

    class Meta:
        model = models.List
        fields = '__all__'


class ListField(serializers.RelatedField):
    def to_representation(self, value):
        return {'id': value.id, 'name': value.name}


class ProjectSerializer(serializers.ModelSerializer):
    lists = ListField(
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
