from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

from django_filters.rest_framework import DjangoFilterBackend

from tasks.serializers import TaskSerializer, TaskDetailSerializer
from tasks.models import Task


class TaskCreateView(generics.CreateAPIView):
    """ Создание Задачи """
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]


class TaskListView(generics.ListAPIView):
    """ Просмотр списка Задач Пользователя по его id """
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['completed']
    pagination_class = PageNumberPagination

    def get_queryset(self):
        user_id = self.kwargs['pk']
        return Task.objects.filter(user=user_id)


class TaskDetailView(generics.RetrieveAPIView):
    """ Просмотр одной Задачи по ее id """
    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializer
    permission_classes = [IsAuthenticated]


class TaskUpdateView(generics.UpdateAPIView):
    """ Изменение Задачи по ее id """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]


class TaskDeleteView(generics.DestroyAPIView):
    """ Удаление Задачи по ее id """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
