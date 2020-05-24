# Generated by Django 3.0.6 on 2020-05-24 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_prescription'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('patient_id', models.CharField(max_length=10)),
                ('patient_name', models.CharField(max_length=100)),
                ('doctor_id', models.CharField(max_length=10)),
                ('doctor_name', models.CharField(max_length=100)),
                ('doctor_fee', models.CharField(default='', max_length=100)),
                ('medicine_fee', models.CharField(default='', max_length=100)),
                ('is_admitted', models.BooleanField(default='')),
                ('bed_charge', models.CharField(default='', max_length=100)),
                ('no_days', models.CharField(default='', max_length=100)),
                ('status', models.CharField(default='Pending', max_length=20)),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.TimeField(auto_now_add=True)),
                ('pending', models.CharField(default=100, max_length=100)),
                ('paid', models.CharField(default=100, max_length=100)),
            ],
            options={
                'db_table': 'appointment',
            },
        ),
    ]