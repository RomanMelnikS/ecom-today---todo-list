# Generated by Django 4.1.6 on 2023-02-05 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания'),
        ),
    ]
