# Generated by Django 3.0.6 on 2020-05-23 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='signupform',
            name='phone_number',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
