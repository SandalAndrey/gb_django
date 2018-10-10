from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import ValidationError


def validate_image(avatar):
    file_size = avatar.file.size
    limit_kb = 999
    if file_size > limit_kb * 1024:
        raise ValidationError("Максимальный размер файла для аватарки - %s KB" % limit_kb)


class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', blank=True, validators=[validate_image])
    age = models.PositiveIntegerField(verbose_name='возраст', blank=True, null=True)

    def set_pass(self, password):
        self.set_password(password)
