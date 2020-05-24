# Generated by Django 3.0.6 on 2020-05-23 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_signupform_blood_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('patient_id', models.CharField(max_length=10)),
                ('patient_name', models.CharField(max_length=100)),
                ('doctor_id', models.CharField(max_length=10)),
                ('doctor_name', models.CharField(max_length=100)),
                ('symptoms', models.CharField(max_length=100)),
                ('prescription', models.CharField(max_length=400)),
                ('date', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'prescription',
            },
        ),
    ]