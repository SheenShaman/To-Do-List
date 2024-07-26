from django.db import models
from django.utils import timezone
from django.utils.timezone import now

from users.models import User


class Task(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    completed = models.BooleanField(default=False, verbose_name='Выполнение')
    created_at = models.DateTimeField(default=now, verbose_name='Дата создания')
    updated_at = models.DateTimeField()

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(Task, self).save(*args, **kwargs)

    def __str__(self):
        return f'Задача {self.title} пользователя {self.user}'

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
