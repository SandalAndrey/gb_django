from django.db import models
from django.utils import timezone
from .choices import SUBJECT_CHOICES


class Message(models.Model):
    fio = models.CharField(max_length=200)
    subject = models.CharField(verbose_name='Тема', max_length=50, choices=SUBJECT_CHOICES, default=1)
    email = models.EmailField(max_length=50, blank=True)
    message = models.TextField(verbose_name='Сообщение')
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '{} - {}:{}'.format(self.fio, self.subject, self.created_date)
