from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import signUpForm,Prescription,Appointment
from django.contrib import messages
from django.contrib.auth.models import User,auth 
from django.core.mail import send_mail
# from collections.forms import ContactForm

# Create your views here.
######################################### Home Page Without Login ################################################### 

def home(request):

    # if request.session.has_key('user_id'):
    #     get_user=signUpForm.objects.get(user_id=request.session['user_id'])  
    #     if get_user.user_type=='doctor':
    #         return render(request,'doctor_home.html',{'get_user':get_user})
    #     elif get_user.user_type=='paient':
    #         return render(request,'patient_home.html',{'get_user':get_user})
    #     elif get_user.user_type=="receptionist":
    #         return render(request,'recep_home.html',{'get_user':get_user})  
    #     elif get_user.user_type=="hr":
    #         return render(request,'hr_home.html',{'get_user':get_user})

    return render(request,'home.html')

######################################### Signup Patient Or Doctor ################################################### 


def signup(request):

    if request.method=="POST":

        first_name= request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        user_type = request.POST['register_as']
        password_error = ""
        email_error = ""
        get_data = signUpForm.objects.all()

        if password!=confirm_password:
            password_error = "Password and confirm password must be same"

        if get_data.filter(email=email).exists():
            email_error = "Email already taken"

        if password_error != "" or email_error != "":
            return render(request,'signup.html',{'first_name_0':first_name,'last_name_0':last_name,'email_0':email,'phone_number_0':phone_number,'user_type_0':user_type,'email_error':email_error,'password_error':password_error})
        else:    
            signup = signUpForm(first_name=first_name,last_name=last_name,email=email,phone_number=phone_number,password=password,user_type=user_type)
            signup.save()
            return redirect('login')

    else:
        return render(request,'signup.html')
    
######################################## Login According to Type of User #################################################### 


def login(request):

    if request.method == "POST":
        
        email = request.POST['email']
        password = request.POST['password']

        try:
            get_user=signUpForm.objects.get(email=email,password=password)
            request.session['user_id'] = get_user.user_id 
            if get_user.user_type=='doctor':
                return render(request,'doctor_home.html',{'get_user':get_user})
            elif get_user.user_type=='patient':
                return render(request,'patient_home.html',{'get_user':get_user})
            elif get_user.user_type=="receptionist":
                return render(request,'recep_home.html',{'get_user':get_user})  
            elif get_user.user_type=="hr":
                return render(request,'hr_home.html',{'get_user':get_user})

        except(NameError,signUpForm.DoesNotExist):
            return render(request,'login.html',{'invalid':'Invalid email or password'})



    else:
        return render(request,'login.html')

####################################### Simple Redirection For Patient <Could Be Merged With Doctor Functions >##################################################### 


def patient_home(request):
    if request.session.has_key('user_id'):
        get_user=signUpForm.objects.get(user_id=request.session['user_id'])  
        return render(request,'patient_home.html',{'get_user':get_user})

    return render(request,'patient_home.html')

def patient_prescription(request):
    get_user=signUpForm.objects.get(user_id=request.session['user_id'])  
    get_all_prescriptions = Prescription.objects.filter(patient_id =str(request.session['user_id'])).order_by('-user_id')
    return render(request,'patient_prescription.html',{'get_user':get_user,'get_all_prescriptions':get_all_prescriptions})

def patient_appointment(request):
    get_user=signUpForm.objects.get(user_id=request.session['user_id'])  

    try:
        get_appointments = Appointment.objects.filter(patient_id=str(get_user.user_id)).order_by('-id')
        # get_appointments = Appointment.objects.filter(patient_id="50")

    except:
        return render(request,'patient_appointment.html',{'get_user':get_user})
        
    return render(request,'patient_appointment.html',{'get_user':get_user,'get_appointments':get_appointments})

def patient_invoice(request):
    get_user=signUpForm.objects.get(user_id=request.session['user_id']) 

    try:
        get_all_appointments = Appointment.objects.filter(patient_id=str(get_user.user_id))
    except:
        return render(request,'patient_invoice.html',{'get_user':get_user})
    return render(request,'patient_invoice.html',{'get_user':get_user,'get_all_appointments':get_all_appointments})

def patient_profile(request,user_id):
    if request.session.has_key('user_id') and request.session['user_id']==int(user_id):
        get_user=signUpForm.objects.get(user_id=request.session['user_id'])  
        return render(request,'patient_profile.html',{'get_user':get_user})
    else:
        return redirect('logout')

###################################### Simple Redirection For Doctor <Could Be Merged With Patient Functions >###################################################### 

def doctor_home(request):
    if request.session.has_key('user_id'):
        get_user=signUpForm.objects.get(user_id=request.session['user_id'])  
        return render(request,'doctor_home.html',{'get_user':get_user})

    return render(request,'home.html')

def doctor_prescription(request):
    get_user=signUpForm.objects.get(user_id=request.session['user_id'])  
    get_all_patients = signUpForm.objects.filter(user_type="patient")
    get_all_prescriptions = Prescription.objects.filter(doctor_id=str(request.session['user_id']))
    return render(request,'doctor_prescription.html',{'get_user':get_user,'get_all_patients':get_all_patients,'get_all_prescriptions':get_all_prescriptions})

def doctor_appointment(request):
    get_user=signUpForm.objects.get(user_id=request.session['user_id'])
    try:
        get_appointment = Appointment.objects.filter(doctor_id=str(get_user.user_id))  
    except:
        # get_appointment = 0 
        return render(request,'doctor_appointment.html',{'get_user':get_user})
    return render(request,'doctor_appointment.html',{'get_user':get_user,'get_appointment':get_appointment})

def doctor_profile(request,user_id):
    if request.session.has_key('user_id') and request.session['user_id']==int(user_id):
        get_user=signUpForm.objects.get(user_id=request.session['user_id'])  
        return render(request,'doctor_profile.html',{'get_user':get_user})
    else:
        return redirect('logout')

###################################### Update Patient or Doctor Profile Information ###################################################### 

def update_user(request,user_id):

    if request.session.has_key('user_id') and request.session['user_id']==int(user_id):
        to_update=signUpForm.objects.get(user_id=request.session['user_id']) 

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        try:
            gender = request.POST['gender']
        except:
            gender=""
        age = request.POST['age']
        address = request.POST['address']
        try:
            blood_group = request.POST['blood_group']
        except:
            blood_group = ""

        case_paper = request.POST['case_paper']

        to_update.first_name = first_name
        to_update.last_name = last_name
        to_update.email = email
        to_update.phone_number = phone_number
        to_update.gender = gender
        to_update.age = age
        to_update.address = address
        to_update.blood_group = blood_group
        to_update.case_paper = case_paper

        to_update.save()

        get_user=signUpForm.objects.get(user_id=request.session['user_id'])

        if get_user.user_type=='patient':
            return redirect('patient_home')
        elif get_user.user_type=='doctor':
            return redirect('doctor_home')


        
    else:
        return redirect('logout')


########################################### Add Prescription #####################################

def add_prescription(request):

    doctor_name = request.POST['doctor_name']
    doctor_id = request.POST['doctor_id']
    symptoms = request.POST['symptoms']
    prescription = request.POST['prescription']
    patient_id = request.POST['patient']

    get_patient_name=signUpForm.objects.get(user_id=int(patient_id))

    patient_name = get_patient_name.first_name+" "+get_patient_name.last_name

    prescription_data = Prescription(patient_id=patient_id,patient_name=patient_name,doctor_id=doctor_id,doctor_name=doctor_name,symptoms=symptoms,prescription=prescription)

    prescription_data.save()

    return redirect('doctor_prescription')


################################################ Receptionist Dashboard #######################################

def recep_home(request):
    return render(request,'recep_home.html')

def recep_dashboard(request):
    get_all_patients = signUpForm.objects.filter(user_type="patient")
    get_all_doctors = signUpForm.objects.filter(user_type="doctor")
    get_pending_appointment = Appointment.objects.filter(status="Pending").count()
    get_completed_appointment = Appointment.objects.filter(status="Completed").count()
    get_all_appointments = Appointment.objects.all().order_by('-id')
    get_all_appointments_count = Appointment.objects.all().count()

    return render(request,'recep_dashboard.html',{'get_all_patients':get_all_patients,'get_all_doctors':get_all_doctors,'get_all_appointments':get_all_appointments,'get_pending_appointment':get_pending_appointment,'get_completed_appointment':get_completed_appointment,'get_all_appointments_count':get_all_appointments_count})
    
def add_appointment(request):

    date = request.POST['date']
    time = request.POST['time']
    patient_id = request.POST['patient']
    doctor_id = request.POST['doctor']
    status = request.POST['status']

    get_patient = signUpForm.objects.get(user_id=int(patient_id))
    get_doctor = signUpForm.objects.get(user_id=int(doctor_id))

    patient_name = get_patient.first_name+" "+get_patient.last_name
    doctor_name = get_doctor.first_name+" "+get_doctor.last_name

    appointment_data = Appointment(patient_id=patient_id,patient_name=patient_name,doctor_id=doctor_id,doctor_name=doctor_name,status=status,time=time,date=date,is_admitted=False)
    appointment_data.save()

    return redirect('recep_dashboard')

def update_appointment(request,id):

    get_appointment_info = Appointment.objects.get(id=int(id))

    return render(request,'update_appointment.html',{'get_appointment_info':get_appointment_info})

def update_appoint(request,id):

    to_update = Appointment.objects.get(id=int(id))

    doctor_fee = request.POST['doctor_fee']
    medicine_fee = request.POST['medicine_fee']
    is_admitted = request.POST['is_admitted']
    bed_charge = request.POST['bed_charge']
    no_days = request.POST['no_days']
    paid = request.POST['paid']
    pending = request.POST['pending']
    total = request.POST['total']
    status = request.POST['status']

    to_update.doctor_fee = doctor_fee
    to_update.medicine_fee = medicine_fee
    to_update.is_admitted = is_admitted
    to_update.bed_charge = bed_charge
    to_update.no_days = no_days
    to_update.paid = paid
    to_update.pending = pending
    to_update.total = total
    to_update.status = status

    to_update.save()

    return redirect('recep_dashboard')



def change_patients(request):
    get_all_patients = signUpForm.objects.filter(user_type="patient").order_by('-user_id')

    return render(request,'change_patient.html',{'get_all_patients':get_all_patients})

def update_patients(request,user_id):
    
    get_user=signUpForm.objects.get(user_id=user_id) 
    return render(request,'update_patients.html',{'get_user':get_user})

def update_patients_recep(request, user_id):

    to_update=signUpForm.objects.get(user_id=user_id) 

    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    phone_number = request.POST['phone_number']

    try:
        gender = request.POST['gender']
    except:
        gender=""
    age = request.POST['age']
    address = request.POST['address']
    try:
        blood_group = request.POST['blood_group']
    except:
        blood_group = ""

    case_paper = request.POST['case_paper']

    to_update.first_name = first_name
    to_update.last_name = last_name
    to_update.email = email
    to_update.phone_number = phone_number
    to_update.gender = gender
    to_update.age = age
    to_update.address = address
    to_update.blood_group = blood_group
    to_update.case_paper = case_paper

    to_update.save()

    return redirect('change_patients')

def add_patients(request):

    return render(request,'add_patients.html')

def add_patients_recep(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    phone_number = request.POST['phone_number']
    user_type="patient"
    password="1234567890"
    try:
        gender = request.POST['gender']
    except:
        gender=""
    age = request.POST['age']
    address = request.POST['address']
    try:
        blood_group = request.POST['blood_group']
    except:
        blood_group = ""

    case_paper = request.POST['case_paper']

    get_data = signUpForm.objects.all()
    if get_data.filter(email=email).exists():
        email_error = "Email already taken"
        return render(request,'add_patients.html',{'first_name':first_name,
                                                        'last_name':last_name,
                                                        'email':email,
                                                        'phone_number':phone_number,
                                                        'gender':gender,
                                                        'age':age,
                                                        'address':address,
                                                        'blood_group':blood_group,
                                                        'case_paper':case_paper,
                                                        'email_error':email_error
                                                        })

    insert_data = signUpForm(first_name=first_name,last_name=last_name,email=email,phone_number=phone_number,user_type=user_type,password=password,gender=gender,age=age,address=address,blood_group=blood_group,case_paper=case_paper)
    insert_data.save()

    return redirect('change_patients')
    
def delete_patients(request,user_id):
    get_user = signUpForm.objects.get(user_id=user_id)

    signUpForm.objects.filter(user_id=user_id).delete()

    
    if get_user.user_type == "patient":
        Prescription.objects.filter(patient_id=user_id).delete()
        Appointment.objects.filter(patient_id=user_id).delete() 
        return redirect('change_patients')
    else:
        Prescription.objects.filter(doctor_id=user_id).delete()
        Appointment.objects.filter(doctor_id=user_id).delete() 
        return redirect('hr_dashbaord')


################################################# Human Resources ####################################################### 

def hr_home(request):
    return render(request,'hr_home.html')

def  hr_dashbaord(request):

    get_all_patients_count = signUpForm.objects.filter(user_type='patient').count()

    get_all_doctors_count = signUpForm.objects.filter(user_type='doctor').count()

    get_all_active_doctors_count = signUpForm.objects.filter(user_type='doctor',status="Active").count()

    get_all_doctors = signUpForm.objects.filter(user_type='doctor').order_by('-user_id')

    return render(request,'hr_dashboard.html',{'get_all_doctors':get_all_doctors,'get_all_patients_count':get_all_patients_count,'get_all_doctors_count':get_all_doctors_count,'get_all_active_doctors_count':get_all_active_doctors_count})

def update_doctor(request,user_id):
    get_user=signUpForm.objects.get(user_id=user_id) 
    return render(request,'update_doctor_form.html',{'get_user':get_user})

def update_doctor_hr(request,user_id):

    to_update=signUpForm.objects.get(user_id=user_id) 

    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    phone_number = request.POST['phone_number']
    gender = request.POST['gender']
    age = request.POST['age']
    address = request.POST['address']
    blood_group = request.POST['blood_group']
    department = request.POST['department']
    salary = request.POST['salary']
    attendance = request.POST['attendance']
    status = request.POST['status']

    to_update.first_name= first_name
    to_update.last_name= last_name
    to_update.email= email
    to_update.phone_number= phone_number
    to_update.gender= gender
    to_update.age= age
    to_update.address= address
    to_update.blood_group= blood_group
    to_update.department= department
    to_update.salary= salary
    to_update.attendance= attendance
    to_update.status= status

    to_update.save()

    return redirect('hr_dashbaord')


def add_doctors(request):

    if request.method=="POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        gender = request.POST['gender']
        age = request.POST['age']
        address = request.POST['address']
        blood_group = request.POST['blood_group']
        department = request.POST['department']
        salary = request.POST['salary']
        attendance = request.POST['attendance']
        status = request.POST['status']
        password = "1234567890"
        user_type = "doctor"

        get_data = signUpForm.objects.all()
        if get_data.filter(email=email).exists():
            email_error = "Email already taken"
            return render(request,'add_doctors_form.html',{'first_name':first_name,
                                                            'last_name':last_name,
                                                            'email':email,
                                                            'phone_number':phone_number,
                                                            'gender':gender,
                                                            'age':age,
                                                            'address':address,
                                                            'blood_group':blood_group,
                                                            'department':department,
                                                            'salary':salary,
                                                            'attendance':attendance,
                                                            'status':status,
                                                            'email_error':email_error
                                                            })

        doctor_info =  signUpForm(first_name=first_name,
                                  last_name=last_name,
                                  email=email,
                                  phone_number=phone_number,
                                  gender=gender,
                                  age=age,
                                  address=address,
                                  blood_group=blood_group,
                                  department=department,
                                  salary=salary,
                                  attendance=attendance,
                                  status=status,
                                  password=password,
                                  user_type=user_type
                                  )
        doctor_info.save()
        return  redirect('hr_dashbaord')

    else:
        return render(request,'add_doctors_form.html')


def hr_accounting(request):
    
    get_all_appointments = Appointment.objects.filter(status="Completed").order_by('-id')
    email_success=""
    email_failed= ""
    if request.session.has_key('email_sent'):
        email_success="Email sent successfully"
        del request.session['email_sent']
    elif request.session.has_key('email_not_sent'):
        email_failed=" Email not sent. Please try again!!!"
        del request.session['email_not_sent']

    return render(request,'hr_accounting.html',{'get_all_appointments':get_all_appointments,'email_success':email_success,'email_failed':email_failed})



        

################################################# Logout ####################################################### 


def logout(request):

    try:
        del request.session['user_id']
        return redirect('login')

    except:
        return redirect('login')


############################################### Send Mail ######################################################

def send_mail_to_remind(request,id):

    get_appoint = Appointment.objects.get(id=int(id))
    get_email = signUpForm.objects.get(user_id=int(get_appoint.patient_id))

    sent = send_mail('Reminder for Payment',
            'Your payment of ID : '+ str(get_appoint.id)+ ' is pending, pending amount Rs.'+get_appoint.pending+'/- of total amount Rs.'+ get_appoint.total+'. Please kindly do the the payment' ,
            'djha9680@gmail.com',
            [get_email.email],
            fail_silently=False,
            )

    if sent:
        request.session['email_sent']="Success"
    else:
        request.session['email_not_sent']="Failed"


    return redirect('hr_accounting')