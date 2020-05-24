from django.db import models

# Create your models here.

class signUpForm(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=10)
    user_type = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    gender=models.CharField(max_length=10,default="")
    age=models.CharField(max_length=4,default="")
    address=models.CharField(max_length=200,default="")
    status = models.CharField(max_length=10,default="Active")
    department = models.CharField(max_length=100,default="")
    attendance = models.CharField(max_length=400,default="")
    salary = models.CharField(max_length=10,default=0)
    # report=models.ImageField()
    case_paper=models.CharField(max_length=10,default="")
    blood_group=models.CharField(max_length=5,default="")





    class Meta:
        db_table='signup'


class Prescription(models.Model):
    user_id = models.AutoField(primary_key=True)
    patient_id = models.CharField(max_length=10)
    patient_name = models.CharField(max_length=100)
    doctor_id = models.CharField(max_length=10)
    doctor_name = models.CharField(max_length=100)
    symptoms = models.CharField(max_length=100)
    prescription = models.CharField(max_length=400)
    date=models.DateField(auto_now_add=True)

    class Meta:
        db_table='prescription'

class Appointment(models.Model):
    id=models.AutoField(primary_key=True)
    patient_id = models.CharField(max_length=10)
    patient_name = models.CharField(max_length=100)
    doctor_id = models.CharField(max_length=10)
    doctor_name = models.CharField(max_length=100)
    doctor_fee = models.CharField(max_length=100,default="")
    medicine_fee = models.CharField(max_length=100,default="")
    is_admitted = models.BooleanField(default=False)
    bed_charge = models.CharField(max_length=100,default="")
    no_days = models.CharField(max_length=100,default="")
    status = models.CharField(max_length=20,default="Pending")
    date=models.CharField(max_length=20,default="")
    time = models.CharField(max_length=15,default="")
    pending = models.CharField(max_length=100,default="")
    paid = models.CharField(max_length=100,default="")
    total = models.CharField(max_length=100,default="")

    class Meta:
        db_table='appointment'



    