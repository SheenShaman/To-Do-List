from rest_framework import serializers

from django.core.validators import MaxLengthValidator

from tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=50, validators=[MaxLengthValidator], allow_null=False)
    completed = serializers.BooleanField(allow_null=False)

    class Meta:
        model = Task
        fields = ['title', 'completed', 'user']


class TaskDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
