from django.db import models
from django.contrib.auth import get_user_model

from catalog.models import Product

UserModel = get_user_model()


class Cart(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, unique=True,
                             db_index=True)
    price = models.IntegerField(default=0)
    count = models.IntegerField(default=0)
    items = models.ManyToManyField(Product, related_name='items')
