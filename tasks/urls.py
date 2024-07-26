from django.urls import path

from tasks.apps import TasksConfig
from tasks.views import TaskCreateView, TaskListView, TaskDetailView, TaskUpdateView, TaskDeleteView

app_name = TasksConfig.name

urlpatterns = [
    path('create/', TaskCreateView.as_view(), name='create'),
    path('list/<int:pk>/', TaskListView.as_view(), name='list'),
    path('detail/<int:pk>/', TaskDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', TaskUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name='delete'),
]
