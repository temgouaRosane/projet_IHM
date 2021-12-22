from django.shortcuts import redirect, render
from django.views.generic.edit import UpdateView, DeleteView
from usermanagement.models import Consultation, Examen, Medicament, Patient
from .formulaire import  MedicineForm, PatientForm, ConsultationForm, ExamForm
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    return render(request, 'usermanagement/index.html')
    

def home(request):
    if request.user.role == "Receptionist":
        return render(request, 'usermanagement/receptionist/receptionist.html')
    elif request.user.role == "Doctor":
        return render(request, 'usermanagement/doctor/doctor.html')
    elif request.user.role == "Pharmacist":
        return render(request, 'usermanagement/pharmacist/pharmacist.html')    
    else:
        return render(request, 'usermanagement/home.html')


def reception(request):
     return render(request, 'usermanagement/description/reception.html')


def about(request):
    return render(request, 'usermanagement/about.html')


def pharmacy(request):
    return render(request, 'usermanagement/description/pharmacy.html')



def addPatient(request):
    #traitement de la requete post
    if request.method == "POST":
        form = PatientForm(request.POST).save()
        return render(request, 'usermanagement/receptionist/viewpatientlist.html') #redirect('/addPatient')
    else:   
        form = PatientForm()    
    return render(request, 'usermanagement/receptionist/addPatient.html', {'form':form})
    #objet formulaire sous forme d'un dictionnaire:{'form':form}


def receptionist(request):
    return render(request, 'usermanagement/receptionist/receptionist.html')



def viewpatientlist(request):
    if request.method == 'POST':
        name = request.POST['name']
        patients = Patient.objects.filter(FirstName__contains=name)
        context = {
            'patients': patients,
            'selectName':name,
        }
        return render(request, 'usermanagement/receptionist/viewpatientlist.html',context=context)
    patients = Patient.objects.all()
    context = {
        'patients': patients,
    }
    return render(request, 'usermanagement/receptionist/viewpatientlist.html', context)



class PatientUpdateView(UpdateView):
    model = Patient
    context = {
        'patients': Patient.objects.all()
    }
    fields = '__all__'
    template_name = 'usermanagement/receptionist/patient_update_form.html'


class PatientDeleteView(DeleteView):
    model = Patient
    success_url = reverse_lazy('usermanagement:viewpatientlist')


def doctor(request):        
    return render(request, 'usermanagement/doctor/doctor.html')


def pharmacist(request):        
    return render(request, 'usermanagement/pharmacist/pharmacist.html')


def doctorviewpl(request):
    if request.method == 'POST':
        name = request.POST['name']
        patients = Patient.objects.filter(FirstName__contains=name)
        context = {
            'patients': patients,
            'selectName':name,
        }
        return render(request, 'usermanagement/doctor/doctorviewpl.html',context=context)

    patients = Patient.objects.all()
    context = {
        'patients': patients,
    }
    return render(request, 'usermanagement/doctor/doctorviewpl.html', context)


def pharmacistviewpl(request):        
    medicaments = Medicament.objects.all()
    listePatient = []
    for m in medicaments:
        if not m.idPatient in listePatient:
            listePatient.append(m.idPatient)
    context = {
        'listePatient':listePatient,
        'medicaments':medicaments,
    }
    return render(request=request,template_name='usermanagement/pharmacist/pharmacistviewpl.html',context=context)


def pharmacist(request):
    pass

class DoctorPatientUpdateView(UpdateView):
    model = Patient
    fields = '__all__'
    template_name = 'usermanagement/doctor/patient_doctor_update_form.html'
    success_url = reverse_lazy('usermanagement:doctorviewpl')


class DoctorPatientDeleteView(DeleteView):
    model = Patient
    success_url = reverse_lazy('usermanagement:doctorviewpl')


def consultationlist(request):
    if request.method == 'POST':
        name = request.POST['name']
        consultations = Consultation.objects.filter(consultation_idPatient_FirstName__contains=name)
        context = {
            'consultations': consultations,
            'selectName':name,
        }
        return render(request, 'usermanagement/doctor/consultationlist.html',context=context)
    consultations = Consultation.objects.all()
    context = {
        'consultations': consultations,
    }
    return render(request, 'usermanagement/doctor/consultationlist.html', context)


def newconsultation(request):
    #traitement de la requete post
    if request.method == "POST":
        form1 =  ConsultationForm(request.POST).save()
        return render(request, 'usermanagement/doctor/doctor.html') #redirect('/addPatient')
    else:   
        form1 = ConsultationForm()    
    return render(request, 'usermanagement/doctor/newconsultation.html', {'form':form1})
    #objet formulaire sous forme d'un dictionnaire:{'form':form}

def newexamprescription(request):
    if request.method == "POST":
        form =  ExamForm(request.POST).save()
        return render(request, 'usermanagement/doctor/doctor.html') #redirect('/addPatient')
    else:   
        form = ExamForm()    
    return render(request, 'usermanagement/doctor/newexamprescription.html', {'form':form})

def prescriptionlist(request):
    if request.method == 'POST':
        name = request.POST['name']
        examens = Examen.objects.filter(consultation_idPatient_FirstName__contains=name)
        medicaments = Medicament.objects.filter(consultation_idPatient_FirstName__contains=name)
        context = {
            'examens': examens,
            'medicaments': medicaments,
            'selectName':name,
        }
        return render(request, 'usermanagement/doctor/prescriptionlist.html',context=context)
    examens = Examen.objects.all()
    medicaments = Medicament.objects.all()
    context = {
            'examens': examens,
            'medicaments': medicaments,
    }
    return render(request, 'usermanagement/doctor/prescriptionlist.html', context)


def newmedicineprescription(request):
    if request.method == "POST":
        form =  MedicineForm(request.POST).save()
        return render(request, 'usermanagement/doctor/doctor.html') #redirect('/addPatient')
    else:   
        form = MedicineForm()    
    return render(request, 'usermanagement/doctor/newmedicineprescription.html', {'form':form})








