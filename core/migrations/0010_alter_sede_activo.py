# Generated by Django 3.2.5 on 2021-07-28 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20210728_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sede',
            name='activo',
            field=models.CharField(default='True', max_length=5, verbose_name='activoSede'),
        ),
    ]
