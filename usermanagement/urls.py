from django.urls import path,include
from .views import *
from usermanagement.views import *
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
    path('patient_update/<int:pk>/', PatientUpdateView, name = 'patient_update'),
    path('patient_confirm_delete/<int:pk>/', PatientDeleteView.as_view(), name = 'patient_confirm_delete'),
    path('NewRegistration/<nom>', NewRegistration, name='NewRegistration'),
    path('patientDetails/<nom>', patientDetails, name='patientDetails'),


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
    path('Result/<id>', Result, name='Result'),
    path('examlist/', examlist, name='examlist'),
    path('medecinelist/', medecinelist, name='medecinelist'),
    path('newmedicineprescription/', newmedicineprescription, name='newmedicineprescription'),
    path('patientActions/<id>', patientActions, name='patientActions'),
    path('sendToSpecialist/<id>', sendToSpecialist, name='sendToSpecialist'),
    path('sendToSpecialistValidation/<id>', sendToSpecialistValidation, name='sendToSpecialistValidation'),

    path('newconsultation2/<id>', newconsultation2, name='newconsultation2'),
    path('newexamprescription2/<id>', newexamprescription2, name='newexamprescription2'),
    path('newmedicineprescription2/<id>', newmedicineprescription2, name='newmedicineprescription2'),


    


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
    path('examshistory2/', examshistory2, name='examshistory2'),
    path('saveExamResult/<id>', saveExamResult, name='saveExamResult'),


#------------------------------------CASHIER-----------------------------------------------#
#------------------------------------CASHIER-----------------------------------------------#
#------------------------------------CASHIER-----------------------------------------------#

    path('cashierviewpl/', cashierviewpl, name='cashierviewpl'),
    path('viewbill/<idPatient>', viewbill, name='viewbill'),
    path('viewconsultationlist/', viewconsultationlist, name='viewconsultationlist'),
    path('cashierviewexam/', cashierviewexam, name='cashierviewexam'),
    path('validation/<id>', validation, name='validation'),
    path('savevalidation/<id>', savevalidation, name='savevalidation'),
    path('savevalidationexams/<id>', savevalidationexams, name='savevalidationexams'),
    path('validationexams/<id>', validationexams, name='validationexams'),
    path('consultationbill/<id>', consultationbill, name='consultationbill'),
    path('cashierhistory/', cashierhistory, name='cashierhistory'),
    path('examshistory/', examshistory, name='examshistory'),




#------------------------------------DENTIST-----------------------------------------------#
#------------------------------------DENTIST-----------------------------------------------#
#------------------------------------DENTIST-----------------------------------------------#
#------------------------------------DENTIST-----------------------------------------------#

    path('dentistviewpl/', dentistviewpl, name='dentistviewpl'),
    path('patient_doctor_update/<int:pk>/', DoctorPatientUpdateView.as_view(), name = 'patient_doctor_update'),
    path('doctor_patient_confirm_delete/<int:pk>/', DoctorPatientDeleteView.as_view(), name = 'doctor_patient_confirm_delete'),
    path('dconsultationlist/', dconsultationlist, name='dconsultationlist'),
    path('dnewconsultation/', dnewconsultation, name='dnewconsultation'),
    path('dnewexamprescription/', dnewexamprescription, name='dnewexamprescription'),
    path('dexamlist/', dexamlist, name='dexamlist'),
    path('dmedecinelist/', dmedecinelist, name='dmedecinelist'),
    path('dnewmedecineprescription/', dnewmedecineprescription, name='dnewmedecineprescription'),
    path('sendToGeneralist/<id>', sendToGeneralist, name='sendToGeneralist'),
    path('sendToGeneralistValidation/<id>', sendToGeneralistValidation, name='sendToGeneralistValidation'),










]
