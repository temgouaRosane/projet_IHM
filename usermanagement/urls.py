from django.urls import path,include

from usermanagement import index1
from .views import *
from usermanagement.views import *
#from . import index1

app_name = 'usermanagement'

urlpatterns = [
    path('', index , name="index"),
    path('home/', home , name="home"),
    path('reception/', reception, name='reception'),
    path('receptionist/', receptionist, name='receptionist'),
    path('about/', about, name='about'),
    path('pharmacy/', pharmacy, name='pharmacy'),
    path('viewpatientlist/', viewpatientlist, name='viewpatientlist'),
    path('addPatient/', addPatient, name='addPatient'),
    path('patient_update/<int:pk>/', PatientUpdateView.as_view(), name = 'patient_update'),
    path('patient_confirm_delete/<int:pk>/', PatientDeleteView.as_view(), name = 'patient_confirm_delete'),
    path('doctor/', doctor, name='doctor'),
    path('pharmacist/', pharmacist, name='pharmacist'),
    path('doctorviewpl/', doctorviewpl, name='doctorviewpl'),
    path('pharmacistviewpl/', pharmacistviewpl, name='pharmacistviewpl'),
    path('patient_doctor_update/<int:pk>/', DoctorPatientUpdateView.as_view(), name = 'patient_doctor_update'),
    path('doctor_patient_confirm_delete/<int:pk>/', DoctorPatientDeleteView.as_view(), name = 'doctor_patient_confirm_delete'),
    path('consultationlist/', consultationlist, name='consultationlist'),
    path('newconsultation/', newconsultation, name='newconsultation'),
    path('newexamprescription/', newexamprescription, name='newexamprescription'),
    path('prescriptionlist/', prescriptionlist, name='prescriptionlist'),
    path('newmedicineprescription/', newmedicineprescription, name='newmedicineprescription'),

    


    




    









]
