#on code le formulaire qui va etre visible via le template
#import de la classe model form qui va creer le formulaire
from django.forms import ModelForm, fields
#import du model Patient. le formulaire va etre creer a partir du modele patient
from .models import Patient
#je creer un classe qui va heriter de la classe modelForm, et c'est elle qui va creer le formulaire d'insertion des does

class PatientForm(ModelForm):
    class Meta:
        model= Patient
        fields = ['numero', 'FirstName', 'LastName', 'sexe', 'Phone_number', 'BirthDate', 'Address', 'Email_address', 'condition', 'Status', 'temperature', 'weight', 'arterialPressure']
