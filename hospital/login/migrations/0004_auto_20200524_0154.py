# Generated by Django 3.0.6 on 2020-05-23 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20200524_0151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signupform',
            name='address',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='signupform',
            name='age',
            field=models.CharField(default='', max_length=4),
        ),
        migrations.AlterField(
            model_name='signupform',
            name='case_paper',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='signupform',
            name='gender',
            field=models.CharField(default='', max_length=10),
        ),
    ]
