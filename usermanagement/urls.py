from django.urls import path,include

from usermanagement import index1
from .views import *
from usermanagement.views import *
#from . import index1

app_name = 'usermanagement'

urlpatterns = [

#---------------------------------DESCRIPTION--------------------------------------#
#---------------------------------DESCRIPTION--------------------------------------#
#---------------------------------DESCRIPTION--------------------------------------#
    path('', index , name="index"),
    path('home/', home , name="home"),
    path('reception/', reception, name='reception'),
    path('about/', about, name='about'),
    path('dentalunit/', dentalunit, name='dentalunit'),
    path('genMedicine/', genMedicine, name='genMedicine'),
    path('laboratory/', laboratory, name='laboratory'),
    path('ophtalmoservice/', ophtalmoservice, name='ophtalmoservice'),
    path('cashdesk/', cashdesk, name='cashdesk'),
    path('pharmacy/', pharmacy, name='pharmacy'),



#-----------------------------------RECEPTIONIST----------------------------------#
#-----------------------------------RECEPTIONIST----------------------------------#
#-----------------------------------RECEPTIONIST----------------------------------#
    path('receptionist/', receptionist, name='receptionist'),
    path('viewpatientlist/', viewpatientlist, name='viewpatientlist'),
    path('addPatient/', addPatient, name='addPatient'),
    path('patient_update/<int:pk>/', PatientUpdateView.as_view(), name = 'patient_update'),
    path('patient_confirm_delete/<int:pk>/', PatientDeleteView.as_view(), name = 'patient_confirm_delete'),
    path('NewRegistration/<nom>,<prenom>,<cni>', NewRegistration, name='NewRegistration'),
    path('patientDetails/<nom>,<prenom>,<cni>', patientDetails, name='patientDetails'),


#------------------------------------------------DOCTOR-----------------------------------#
#------------------------------------------------DOCTOR-----------------------------------#
#------------------------------------------------DOCTOR-----------------------------------#
    path('doctor/', doctor, name='doctor'),
    path('doctorviewpl/', doctorviewpl, name='doctorviewpl'),
    path('patient_doctor_update/<int:pk>/', DoctorPatientUpdateView.as_view(), name = 'patient_doctor_update'),
    path('doctor_patient_confirm_delete/<int:pk>/', DoctorPatientDeleteView.as_view(), name = 'doctor_patient_confirm_delete'),
    path('consultationlist/', consultationlist, name='consultationlist'),
    path('newconsultation/', newconsultation, name='newconsultation'),
    path('newexamprescription/', newexamprescription, name='newexamprescription'),
    path('examlist/', examlist, name='examlist'),
    path('medecinelist/', medecinelist, name='medecinelist'),
    path('newmedicineprescription/', newmedicineprescription, name='newmedicineprescription'),


#------------------------------------PHARMACIST-----------------------------------------------#
#------------------------------------PHARMACIST-----------------------------------------------#
#------------------------------------PHARMACIST-----------------------------------------------#
    path('pharmacistviewpl/', pharmacistviewpl, name='pharmacistviewpl'),
    path('pharmacist/', pharmacist, name='pharmacist'),
    path('facturemedicament/<id>', facturemedicament, name='facturemedicament'),


#------------------------------------LAB_TECHNICIAN-----------------------------------------------#
#------------------------------------LAB_TECHNICIAN-----------------------------------------------#
#------------------------------------LAB_TECHNICIAN-----------------------------------------------#

    path('labtechviewpl/', labtechviewpl, name='labtechviewpl'),
    path('factureexamen/<id>', factureexamen, name='factureexamen'),


#------------------------------------CASHIER-----------------------------------------------#
#------------------------------------CASHIER-----------------------------------------------#
#------------------------------------CASHIER-----------------------------------------------#

    path('cashierviewpl/', cashierviewpl, name='cashierviewpl'),
    path('viewbill/<idPatient>', viewbill, name='viewbill'),


#------------------------------------DENTIST-----------------------------------------------#
#------------------------------------DENTIST-----------------------------------------------#
#------------------------------------DENTIST-----------------------------------------------#
#------------------------------------DENTIST-----------------------------------------------#

    path('dentistviewpl/', dentistviewpl, name='dentistviewpl'),
    path('patient_doctor_update/<int:pk>/', DoctorPatientUpdateView.as_view(), name = 'patient_doctor_update'),
    path('doctor_patient_confirm_delete/<int:pk>/', DoctorPatientDeleteView.as_view(), name = 'doctor_patient_confirm_delete'),
    path('dconsultationlist/', dconsultationlist, name='dconsultationlist'),
    path('dnewconsultation/', dnewconsultation, name='dnewconsultation'),
    path('dnewexamprescription/', newexamprescription, name='dnewexamprescription'),
    path('dexamlist/', dexamlist, name='dexamlist'),
    path('dmedecinelist/', medecinelist, name='dmedecinelist'),
    path('dnewmedecineprescription/', dnewmedecineprescription, name='dnewmedecineprescription'),









]
