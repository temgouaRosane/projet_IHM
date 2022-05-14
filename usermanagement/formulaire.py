#on code le formulaire qui va etre visible via le template
#import de la classe model form qui va creer le formulaire
from django.forms import ModelForm, fields
#import du model Patient. le formulaire va etre creer a partir du modele patient
from .models import Consultation, Examen, Medicament, Patient
#je creer un classe qui va heriter de la classe modelForm, et c'est elle qui va creer le formulaire d'insertion des does
from django import forms
class DateInput(forms.DateInput):
    input_type='date'

class PatientForm(ModelForm):
    class Meta:
        model= Patient
        fields = ['FirstName', 'LastName', 'gender', 'BirthDate', 'Address','CNI_number','Phone_number', 'Email_address', 'condition', 'Service', 'ConsultationCost']

        widgets={
            'BirthDate': DateInput(),
        }

class ConsultationForm(ModelForm):
    class Meta:
        model= Consultation
        fields = ['consultationCost', 'idPatient', 'consultation_reason', 'allergy', 'previous_history','weight', 'height', 'temperature', 'arterialpressure','skin_appearence', 'Consultation_Notes' ]

class ExamForm(ModelForm):
    class Meta:
        model= Examen
        fields = ['idPatient', 'ExamDescription', 'ExamCost']

class MedicineForm(ModelForm):
    class Meta:
        model= Medicament
        fields = ['idPatient', 'MedicineName', 'MedicineCost']