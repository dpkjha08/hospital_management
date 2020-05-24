"""hospital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('doctor_home/',views.doctor_home,name='doctor_home'),
    path('patient_home/',views.patient_home,name='patient_home'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('prescription/',views.patient_prescription,name="prescription"),
    path('appointment/',views.patient_appointment,name="appointment"),
    path('invoice/',views.patient_invoice,name="invoice"),
    path('patient_profile/<user_id>',views.patient_profile,name="patient_profile"),
    path('doctor_prescription/',views.doctor_prescription,name="doctor_prescription"),
    path('doctor_appointment/',views.doctor_appointment,name="doctor_appointment"),
    path('doctor_profile/<user_id>',views.doctor_profile,name="doctor_profile"),
    path('update_user/<user_id>',views.update_user,name="update_user"),
    path('add_prescription/',views.add_prescription,name="add_prescription"),
    path('recep_dashboard/',views.recep_dashboard,name="recep_dashboard"),
    path('recep_home/',views.recep_home,name="recep_home"),
    path('add_appointment/',views.add_appointment,name="add_appointment"),
    path('update_appointment/<id>',views.update_appointment,name='update_appointment'),
    path('update_appoint/<id>',views.update_appoint,name='update_appoint'),
    path('change_patients/',views.change_patients,name='change_patients'),
    path('update_patients/<user_id>',views.update_patients,name='update_patients'),
    path('update_patients_recep/<user_id>',views.update_patients_recep,name='update_patients_recep'),
    path('add_patients/',views.add_patients,name='add_patients'),
    path('add_patients_recep',views.add_patients_recep,name='add_patients_recep'),
    path('delete_patients/<user_id>',views.delete_patients,name='delete_patients'),
    path('hr_home/',views.hr_home,name='hr_home'),
    path('hr_dashbaord/',views.hr_dashbaord,name='hr_dashbaord'),
    path('hr_accounting/',views.hr_accounting,name='hr_accounting'),
    path('update_doctor/<user_id>',views.update_doctor,name='update_doctor'),
    path('update_doctor_hr/<user_id>',views.update_doctor_hr,name='update_doctor_hr'),
    path('add_doctors/',views.add_doctors,name='add_doctors'),
    path('send_mail_to_remind/<id>',views.send_mail_to_remind,name='send_mail_to_remind'),
    path('logout/',views.logout,name='logout')

    # path('bar',include('login.urls')),
    # path('admin/', admin.site.urls),
]
