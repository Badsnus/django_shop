# Generated by Django 3.2.16 on 2022-10-30 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cart',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]