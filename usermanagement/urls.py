from django.urls import path,include

from usermanagement import index1
from .views import *
from usermanagement import views
#from . import index1

app_name = 'usermanagement'

urlpatterns = [
    path('', index , name="index"),
    path('home/', home , name="home"),
    path('reception/', reception, name='reception'),
    path('about/', about, name='about'),
    path('pharmacy/', pharmacy, name='pharmacy'),
    path('viewpatientlist/', views.viewpatientlist, name='viewpatientlist'),
    path('addPatient/', addPatient, name='addPatient'),
    path('patient_update/<int:pk>/', PatientUpdateView.as_view(), name = 'patient_update'),
    path('patient_confirm_delete/<int:pk>/', PatientDeleteView.as_view(), name = 'patient_confirm_delete'),


    




    









]
