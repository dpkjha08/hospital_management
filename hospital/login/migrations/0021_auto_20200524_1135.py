# Generated by Django 3.0.6 on 2020-05-24 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0020_prescription_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='date',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]