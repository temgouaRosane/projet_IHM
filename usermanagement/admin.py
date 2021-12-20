from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from .models import *
 

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'is_staff']
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Profile',
            {
                'fields':(
                    'role',
                )
            }
        )
    )
    
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Patient)
admin.site.register(Consultation)
admin.site.register(Maladie)
admin.site.register(Prescription)
admin.site.register(Medicament)
admin.site.register(Examen)
admin.site.register(Departement)
admin.site.register(Recu)
admin.site.register(LingneRecu)
admin.site.register(Visite)
admin.site.register(Salle)
admin.site.register(Visiteur)
admin.site.register(Employe)
admin.site.register(Symptome)
admin.site.register(Rendez_vous)
admin.site.register(Diagnostiquer) 
admin.site.register(Avoir1)
admin.site.register(Prescrire)
admin.site.register(Suivre)
admin.site.register(Avoir2)
admin.site.register(Detecter)
admin.site.register(Donner)
admin.site.register(Prescrire1)
admin.site.register(Prescrire2)



