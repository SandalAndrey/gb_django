from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


# class MyUserManager(BaseUserManager):
#
#     def create_user(self, username, avatar=None, age=None, password=None):
#         user = self.model(
#             username=username,
#             avatar=avatar,
#             age=age,
#         )
#
#         user.set_password(password)
#         user.save(using=self._db)
#
#         return user
#
#     def create_superuser(self, username, avatar, age, password):
#         user = self.create_user(
#             username = username,
#             avatar=avatar,
#             age=age,
#         )
#         user.is_admin = True
#         user.save(using=self._db)
#
#         return user


class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', blank=True)
    age = models.PositiveIntegerField(verbose_name='возраст', blank=True, null=True)

    def set_pass(self, password):
        self.set_password(password)
