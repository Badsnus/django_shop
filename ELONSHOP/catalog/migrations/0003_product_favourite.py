# Generated by Django 3.2.16 on 2022-10-29 08:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0002_alter_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='favourite',
            field=models.ManyToManyField(related_name='favourite', to=settings.AUTH_USER_MODEL),
        ),
    ]