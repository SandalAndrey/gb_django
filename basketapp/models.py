from django.db import models
from django.conf import settings
from productsapp.models import Good


class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='basket')
    product = models.ForeignKey(Good, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)
    # price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    add_datetime = models.DateTimeField(verbose_name='время', auto_now_add=True)
