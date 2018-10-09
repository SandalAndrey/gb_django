from django.db import models
from django.utils import timezone
from contactsapp.choices import SUBJECT_CHOICES


class Message(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    subject = models.CharField(verbose_name='Тема', max_length=50, choices=SUBJECT_CHOICES, default=1)
    email = models.EmailField(max_length=50, blank=True)
    message = models.TextField(verbose_name='Сообщение')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {}:{}'.format(self.name, self.subject, self.created)
