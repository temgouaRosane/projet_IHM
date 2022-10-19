from datetime import timezone
from operator import mod
from tkinter.tix import Tree
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.forms.widgets import Select
from django.utils import tree, timezone
from multiselectfield import MultiSelectField
from django.urls import reverse, reverse_lazy
from django import forms
from datetime import datetime


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
    ('Male', 'Male'),
    ('Female', 'Female'),
]

CONDITION = [
    ('NoCritical', 'NoCritical'),
    ('Critical', 'Critical'),
]

SERVICE = [

    ('Generalist', 'Generalist'),
    ('Specialist', 'Specialist'),

]

class CustomUser(AbstractUser):
    role = models.CharField(max_length=20, default='NoRole', choices=Roles)

    def __str__(self):
        return self.username


class Patient(models.Model):
    Date = models.DateField(auto_now=True,  blank=True)
    Time = models.TimeField(auto_now=True,  blank=True)
    CNI_number = models.CharField(max_length=20,  blank=True, default=" ")
    FirstName = models.CharField(max_length=50,  blank=True)
    LastName = models.CharField(max_length=50,  blank=True, default=" ")
    gender = models.CharField(
    max_length=50, choices=SEXE, default='Male',  blank=True)
    Phone_number = models.CharField(max_length=100,  blank=True, default=" ")
    BirthDate = models.DateField(blank=True, null=True, default="0000-00-00")
    Address = models.CharField(max_length=25,  blank=True, default=" ")
    Email_address = models.CharField(max_length=25, blank=True, default=" ")
    condition = models.CharField(
        max_length=50, choices=CONDITION, default='NoCritical')
    Service = models.CharField(
        max_length=50, choices=SERVICE, default='Generalist')
    ConsultationCost = models.CharField(max_length=23, blank=True)
    status = models.CharField(max_length=20, default="invalid")
    sentStatus = models.CharField(max_length=50, default='notSent')

    def __str__(self):
        return self.FirstName.__str__()+' '+self.LastName.__str__()


class Consultation(models.Model):
    consultationDate = models.DateField(auto_now=True)
    Time = models.TimeField(auto_now=True)
    consultationCost = models.FloatField(blank=True, null=True)
    idPatient = models.ForeignKey(
        "Patient", on_delete=models.CASCADE, null=False, blank=True)
    consultation_reason = models.CharField(max_length=100, blank=True)
    allergy = models.CharField(max_length=1000, null=True, blank=True)
    previous_history = models.CharField(max_length=200, null=True, blank=True)
    weight = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    temperature = models.FloatField(blank=True, null=True)
    arterialpressure = models.FloatField(blank=True, null=True)
    skin_appearence = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=20, default="invalid")
    Consultation_Notes = models.TextField(blank=True, null=True, max_length=100000)

    def __str__(self):
        return self.idPatient.__str__()


class Medicament(models.Model):
    Time = models.TimeField(auto_now=True)
    Date = models.DateField(auto_now=True)
    MedicineName = models.CharField(max_length=50, null=True)

    MedicineCost = models.FloatField()
    idPatient = models.ForeignKey(
        "Patient", on_delete=models.CASCADE, null=False)
    status = models.CharField(max_length=20, default="invalid")

    def __str__(self):
        return self.MedicineName.__str__()+" "+self.idPatient.__str__()


class Examen(models.Model):
    Time = models.TimeField(auto_now=True)
    Date = models.DateField(auto_now=True)
    ExamDescription = models.CharField(max_length=50, null=True)
    ExamCost = models.CharField(max_length=23, blank=True, null=True)
    idPatient = models.ForeignKey(
        "Patient", on_delete=models.CASCADE, null=False)
    status = models.CharField(max_length=20, default="invalid")
    pstatus = models.CharField(max_length=20, default="invalid")
    Notes = models.TextField(max_length=10000, blank=True, null=True)
    ExamResult = models.TextField(max_length=1000, blank=True, null=True)

    def __str__(self) -> str:
        return str(self.idPatient)+' '+str(self.ExamDescription)



class Drog(models.Model):
    medecineName = models.CharField(max_length=100)
    medecineCoast = models.FloatField()
    
class Exam(models.Model):
    examName = models.CharField(max_length=100)
    examCoast = models.FloatField()