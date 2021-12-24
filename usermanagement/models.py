from datetime import timezone
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.forms.widgets import Select
from django.utils import tree, timezone
from multiselectfield import MultiSelectField
from django.urls import reverse, reverse_lazy


User = settings.AUTH_USER_MODEL
# Create your models here.
Roles = [
    ('NoRole', 'NoRole'),
    ('Doctor', 'Doctor'),
    ('Patient', 'Patient'),
    ('Receptionist', 'Receptionist'),
    ('Admin', 'Admin'),
    ('Accountant', 'Accountant'),
    ('Nurse', 'Nurse'),
    ('Labtech', 'Labtech'),
    ('HRM', 'HRM'),
    ('Specialist', 'Specialist'),
    ('Ophtalmologist', 'Ophtalmologist'),
    ('Pharmacist', 'Pharmacist'),
    ('Dentist', 'Dentist'),

]

SEXE = [
        ('Male', 'Male' ),
        ('Female', 'Female' ),
        ]

CONDITION = [
    ('NoCritical', 'NoCritical'),
    ('Critical', 'Critical'),
]

STATUS =(
    ('Married', 'Married'),
    ('Single', 'Single'),
    ('Student', 'Student'),
    ('other', 'other'),
)



SERVICE = [
   
    ('Dental', 'Dental'),
    ('General Medicine', 'General Medicine'),
    ('Opthalmogical', 'Opthalmogical'),
    ('Pediatric', 'pediatric'),

]


class CustomUser(AbstractUser):
    role = models.CharField(max_length=20, default='NoRole', choices = Roles)
    
    def __str__(self):
        return self.username 

class Patient(models.Model):
    Date = models.DateField(auto_now=True)
    Time = models.TimeField(auto_now=True)
    CNI_number = models.CharField(max_length=20)
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    sexe = models.CharField(max_length=50, choices=SEXE, default='Male')
    Phone_number = models.CharField(max_length=100)
    BirthDate = models.DateField()    
    Address = models.CharField(max_length=25)
    Email_address = models.CharField(max_length=25)
    condition = models.CharField(max_length=50, choices=CONDITION, default='NoCritical')
    Service = models.CharField(max_length=50, choices=SERVICE, null=True)
    #temperature = models.FloatField(blank= True, null= True)
    #weight = models.FloatField(blank= True, null= True)
    #arterialPressure = models.FloatField(blank= True, null= True)
    #Note = models.TextField(blank= True, null= True)
    
    
    def __str__(self):
        return str(self.id)+':'+self.FirstName+' '+self.LastName


    def get_absolute_url(self):
        return reverse('usermanagement:viewpatientlist')


class Consultation(models.Model):
    consultationDate = models.DateField(auto_now=True)
    Time = models.TimeField(auto_now=True)
    consultationCost = models.FloatField(blank=True, null=True)
    idPatient = models.ForeignKey("Patient", on_delete=models.CASCADE, null= False)
    consultation_reason = models.CharField(max_length=100)
    allergy = models.CharField(max_length=100)
    previous_history = models.CharField(max_length=200)
    weight = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    temperature = models.FloatField()
    arterialpressure = models.FloatField()
    skin_appearence = models.CharField(max_length=100)

    def __str__(self):
        return self.idPatient.__str__()




class Maladie(models.Model):
    diseaseName = models.CharField(max_length=10)
    description = models.TextField( default= None)


class Prescription(models.Model):
    prescriptionNumber = models.IntegerField()
    StartDate= models.DateField()
    EndDate= models.DateField()


class Medicament(models.Model):
    Time = models.TimeField(auto_now=True)
    Date = models.DateField(auto_now=True)
    MedicineName = models.CharField(max_length=30)
    MedicineCost = models.FloatField()
    idPatient = models.ForeignKey("Patient", on_delete=models.CASCADE, null= False)
    status = models.CharField(max_length=20, default="invalid")


class Examen(models.Model):
    Time = models.TimeField(auto_now=True)
    Date = models.DateField(auto_now=True)
    ExamDescription = models.CharField(max_length=200)
    ExamCost = models.FloatField()
    idPatient = models.ForeignKey("Patient", on_delete=models.CASCADE, null= False)


class Departement(models.Model):
    nomDepaartement = models.TextField()

    

class Recu(models.Model):
    montant = models.IntegerField()
    idPrescription = models.ForeignKey("Prescription", on_delete=models.CASCADE, null= False)


class LingneRecu(models.Model):
    idRecu = models.ForeignKey("Recu", on_delete=models.CASCADE, null= False)


class Visite(models.Model):
    nomVisiteur = models.TextField()
    date = models.DateField()
    heureArrivee = models.TimeField()
    heureDepart = models.TimeField()


class Salle(models.Model):
        idDepartement = models.ForeignKey("Departement", on_delete=models.CASCADE, null= False)


class Visiteur(models.Model):
    nomVisiteur = models.TextField()


class Employe(models.Model):
    nomEmploye = models.TextField()
    PrenomEmploye = models.TextField()
    Poste = models.TextField()
    idDepartement = models.ForeignKey("Departement", on_delete=models.CASCADE, null= False)


class Symptome(models.Model):
    typeSymptome = models.TextField()
    decription = models.TextField()


class Rendez_vous(models.Model):
    date = models.DateField()
    HeureRendez_vous = models.DateTimeField()
    idPatient = models.ForeignKey("Patient", on_delete=models.CASCADE, null= False)
    idEmploye = models.ForeignKey("Employe", on_delete=models.CASCADE, null= False)


class Diagnostiquer(models.Model):
    idMaladie = models.ForeignKey("Maladie", on_delete=models.CASCADE, null= False)
    idConsultation = models.ForeignKey("Consultation", on_delete=models.CASCADE, null= False)


class Avoir1(models.Model):
    idPatient =  models.ForeignKey("Patient", on_delete=models.CASCADE, null= False)
    idMaladie =  models.ForeignKey("Maladie", on_delete=models.CASCADE, null= False)


class Prescrire(models.Model):
    idPatient =  models.ForeignKey("Patient", on_delete=models.CASCADE, null= False)
    idMedicament =  models.ForeignKey("Medicament", on_delete=models.CASCADE, null= False)


class Suivre(models.Model):
    idPatient =  models.ForeignKey("Patient", on_delete=models.CASCADE, null= False)
    idEmploye =  models.ForeignKey("Employe", on_delete=models.CASCADE, null= False)


class Avoir2(models.Model):
    idPatient =  models.ForeignKey("Patient", on_delete=models.CASCADE, null= False)
    idVisite =  models.ForeignKey("Visite", on_delete=models.CASCADE, null= False)


class Detecter(models.Model):
    idConsultation = models.ForeignKey("Consultation", on_delete=models.CASCADE, null= False)
    idSymptome = models.ForeignKey("Symptome", on_delete=models.CASCADE, null= False)


class Donner(models.Model):
    idConsultation = models.ForeignKey("Consultation", on_delete=models.CASCADE, null= False)
    idPrescription = models.ForeignKey("Prescription", on_delete=models.CASCADE, null= False)


class Prescrire1(models.Model):
    idMedicament = models.ForeignKey("Medicament", on_delete=models.CASCADE, null= False)
    idPrescription = models.ForeignKey("Prescription", on_delete=models.CASCADE, null= False)


class Prescrire2(models.Model):
    idPrescription = models.ForeignKey("Prescription", on_delete=models.CASCADE, null= False)
    idExamen = models.ForeignKey("Examen", on_delete=models.CASCADE, null= False)