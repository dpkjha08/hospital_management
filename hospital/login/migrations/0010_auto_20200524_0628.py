# Generated by Django 3.0.6 on 2020-05-24 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0009_auto_20200524_0559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.DateField(default='', max_length=15),
        ),
    ]
