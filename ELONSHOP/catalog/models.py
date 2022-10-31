from django.db import models
from django.contrib.auth.admin import User


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1500)
    price = models.IntegerField()
    img = models.ImageField(upload_to='product/%Y/%m/%d/')
    favourite = models.ManyToManyField(User, related_name='favourite')

    def in_favourite(self, user: str) -> bool:
        return bool(self.favourite.filter(favourite__favourite__username=user))

    def __str__(self):
        return f'Продукт № {self.pk}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('name', )

