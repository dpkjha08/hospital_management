# Generated by Django 3.0.6 on 2020-05-24 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_appointment'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='total',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='paid',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='pending',
            field=models.CharField(default='', max_length=100),
        ),
    ]
