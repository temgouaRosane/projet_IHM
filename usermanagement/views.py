from enum import auto
from multiprocessing import context
from django.shortcuts import redirect, render
from django.views.generic.edit import UpdateView, DeleteView
from flask import render_template
from usermanagement.models import Consultation, Drog, Examen, Medicament, Patient, Exam
from .formulaire import  MedicineForm, PatientForm, ConsultationForm, ExamForm
from django.urls import reverse_lazy
from django.http import HttpResponse
import datetime
from datetime import datetime
from django.core.paginator import Paginator
from usermanagement.models import Patient
from django.core.mail import send_mail

# Create your views here.


#---------------------------------------------DESCRIPTION-----------------------------------------#
#---------------------------------------------DESCRIPTION-----------------------------------------#
#---------------------------------------------DESCRIPTION-----------------------------------------#
def index(request):
    return render(request, 'usermanagement/description/index.html')    

def home(request):
    if request.user.role == "Receptionist":
        return viewpatientlist(request)
    elif request.user.role == "Doctor":
        return doctorviewpl(request)
    elif request.user.role == "Pharmacist":
        return pharmacistviewpl(request)  
    elif request.user.role == "Labtech":
        return labtechviewpl(request)  
    elif request.user.role == "Accountant":
        return viewconsultationlist(request)  
    elif request.user.role == "Dentist":
        return dentistviewpl(request)
    else:
        return render(request, 'usermanagement/home.html')


def reception(request):
     return render(request, 'usermanagement/description/reception.html')


def about(request):
    return render(request, 'usermanagement/description/about.html')


def pharmacy(request):
    return render(request, 'usermanagement/description/pharmacy.html')

def cashdesk(request):
    return render(request, 'usermanagement/description/cashdesk.html' )

def laboratory(request):
    return render(request, 'usermanagement/description/laboratory.html' )

def dentalunit(request):
    return render(request, 'usermanagement/description/dentalunit.html' )

def genMedicine(request):
    return render(request, 'usermanagement/description/genMedicine.html' )

def ophtalmoservice(request):
    return render(request, 'usermanagement/description/ophtalmoservice.html' )


#-------------------------------------RECEPTIONIST-----------------------------------------#
#-------------------------------------RECEPTIONIST-----------------------------------------#
#-------------------------------------RECEPTIONIST-----------------------------------------#

def addPatient(request):
    #traitement de la requete post
   
    if request.method == "POST":
        p = Patient()
        p.FirstName = request.POST['FirstName']
        p.LastName = request.POST['LastName']
        p.Phone_number = request.POST['Phone_number']
        p.BirthDate = request.POST['BirthDate']
        p.Address = request.POST['Address']
        p.Email_address = request.POST['Email_address']
        p.ConsultationCost = request.POST['ConsultationCost']
        p.status = 'invalid'
        p.gender = request.POST['sexe']
        p.Service = request.POST['Service']
        p.condition = request.POST['condition']
        print(request.POST['sexe'])
        p.save()
        print('-----------------------------------------------------------')
        print('-----------------------------------------------------------')
        print('-----------------------------------------------------------')
        return viewpatientlist(request) #redirect('/addPatient')
    else:   
        form = PatientForm()
        context={
            'current_date': datetime.now().date().__str__(),
            'form':form
        }
    return render(request, 'usermanagement/receptionist/addPatient.html', context=context)
    #objet formulaire sous forme d'un dictionnaire:{'form':form}
    
    


def receptionist(request):
    return render(request, 'usermanagement/receptionist/receptionist.html')


def viewpatientlist(request):
    name = ''
    if request.method == 'POST':
        if 'name' in request.POST:
            name = request.POST['name']
        patients = Patient.objects.filter(FirstName__contains=name).order_by("Date")[::-1]
        paginator = Paginator(patients, 5)
        page = request.GET.get('page')
        patients = paginator.get_page(page)
        patientList = []
        patientList2 = []
        for p in patients:
            if not [p.FirstName,p.LastName,p.CNI_number] in patientList:
                patientList2.append(p)
                patientList.append([p.FirstName,p.LastName,p.CNI_number])
                
        context = {
            'patientList':patientList,
            'patients': patients,
            'selectName':name,
            
            }
        return render(request, 'usermanagement/receptionist/viewpatientlist.html', context)
    patients = Patient.objects.all().order_by("Date")[::-1]
    paginator = Paginator(patients, 5)
    page = request.GET.get('page')
    patients = paginator.get_page(page)
    patientList = []
    for p in patients:
        if not [p.FirstName,p.LastName,p.CNI_number] in patientList:
            patientList.append([p.FirstName,p.LastName,p.CNI_number])
           
    context = {
        'patientList':patientList,
        'patients': patients,
        
    }
    return render(request, 'usermanagement/receptionist/viewpatientlist.html', context)

def PatientUpdateView(request,pk):
    if request.method=='POST':
        patient= Patient.objects.filter(id__iexact=pk)[0]
        form= PatientForm(request.POST)
        if form.is_valid():
            patient.FirstName= form.cleaned_data['FirstName']
            patient.LastName= form.cleaned_data['LastName']
            patient.gender= form.cleaned_data['gender']
            patient.BirthDate= form.cleaned_data['BirthDate']
            patient.Address= form.cleaned_data['Address']
            patient.CNI_number= form.cleaned_data['CNI_number']
            patient.Phone_number= form.cleaned_data['Phone_number']
            patient.Email_address= form.cleaned_data['Email_address']
            patient.condition= form.cleaned_data['condition']
            patient.Service= form.cleaned_data['Service']
            patient.ConsultationCost= form.cleaned_data['ConsultationCost']
            patient.FirstName= form.cleaned_data['FirstName']
            patient.FirstName= form.cleaned_data['FirstName']
            patient.save()
    return render(request, 'usermanagement/receptionist/patient_update_form.html')



class PatientDeleteView(DeleteView):
    model = Patient
    success_url = reverse_lazy('usermanagement:viewpatientlist')

def NewRegistration(request,nom):
    if request.method == 'POST':
        PatientForm(request.POST).save()
        return viewpatientlist(request)
    p = Patient.objects.filter(FirstName=nom)
    if not p is None:
        p = p[0]
        form = PatientForm(initial={
            'FirstName': p.FirstName.__str__(),
            'LastName': p.LastName.__str__(),
            'gender': p.gender.__str__(),
            'BirthDate': p.BirthDate.__str__(),
            'CNI_number': p.CNI_number.__str__(),
            'Address': p.Address.__str__(),
            'Phone_number': p.Phone_number.__str__(),
            'Email_address': p.Email_address.__str__(),
            })
        date = p.BirthDate.__str__()
        context = {'form':form,'p':p,'date':date}
        return render(request=request,template_name='usermanagement/receptionist/NewRegistration.html',context=context)
    return render(request=request,template_name='usermanagement/receptionist/NewRegistration.html')

def patientDetails(request,nom):
    p = Patient.objects.filter(FirstName=nom)
    context = {'p':p[0],'patients':p}
    if request.user.role == "Receptionist":
        return render(request, 'usermanagement/receptionist/patientDetails.html',context)
    if request.user.role == "Doctor":
        return render(request, 'usermanagement/doctor/patientDetails.html',context)
    return home(request)
    

#'''---------------------------------------------------------------------------------------DOCTOR--------------------------------------'''
#'''---------------------------------------------------------------------------------------DOCTOR--------------------------------------'''
#'''---------------------------------------------------------------------------------------DOCTOR--------------------------------------'''

def doctor(request):        
    return render(request, 'usermanagement/doctor/doctor.html')

def sendToSpecialistValidation(request, id):
    p = Patient.objects.filter(id__exact=id)[0]
    context={
            "p": p
        }     
    return render(request, 'usermanagement/doctor/sendToSpecialistValidation.html', context=context)



def sendToSpecialist(request, id):
    p = Patient.objects.filter(id__iexact=id)[0]
    p.sentStatus = "sent"
    p.Service = "specialist"
    p.save()
    context={
        "p":p
    }
    return render(request, 'usermanagement/doctor/sendToSpecialist.html', context=context)




def doctorviewpl(request):
    if request.method == 'POST':
        name = ''
        if 'name' in request.POST:
            name = request.POST['name']
        patients = Patient.objects.filter(FirstName__contains=name,Service__iexact="generalist",status__iexact="valid").order_by("Date")[::-1]
        paginator = Paginator(patients, 5)
        page = request.GET.get('page')
        patients = paginator.get_page(page)
        patientList = []
        for p in patients:
            if not [p.id,p.FirstName,p.LastName,p.CNI_number] in patientList:
                patientList.append([p.id,p.FirstName,p.LastName,p.CNI_number])
        context = {
            'patientList':patientList,
            'patients': patients,
            'selectName':name,
        }
        return render(request, 'usermanagement/doctor/doctorviewpl.html', context)
    patients = Patient.objects.filter(Service__iexact="generalist",status__iexact="valid").order_by("Date")[::-1]
    paginator = Paginator(patients, 5)
    page = request.GET.get('page')
    patients = paginator.get_page(page)
    patientList = []
    for p in patients:
        if not [p.id,p.FirstName,p.LastName,p.CNI_number] in patientList:
            patientList.append([p.id,p.FirstName,p.LastName,p.CNI_number])

    context = {
        'patientList':patientList,
        'patients': patients,
    }
    return render(request, 'usermanagement/doctor/doctorviewpl.html', context)


class DoctorPatientUpdateView(UpdateView):
    model = Patient
    fields = '__all__'
    template_name = 'usermanagement/doctor/patient_doctor_update_form.html'
    success_url = reverse_lazy('usermanagement:doctorviewpl')


class DoctorPatientDeleteView(DeleteView):
    model = Patient
    success_url = reverse_lazy('usermanagement:doctorviewpl')


def consultationlist(request):
    def contain(patientList,nom,prenom,cni):
        for n,p,c,l in patientList:
            if n==nom and p == prenom and c == cni:
                return False
        return True
    name = ''
    if request.method == 'POST':
        if 'name' in request.POST:
            name = request.POST['name']
    paginator = Paginator(patients, 5)
    page = request.GET.get('page')
    patients = paginator.get_page(page)
    patientList = []
    patientList2 = []
    patients = Patient.objects.filter(FirstName__contains = name)
    
    listId = []
    for p in patients:
        patientList2.append[p]
        listId.append(p.id) 
        

    consultations = Consultation.objects.filter(idPatient__in=listId)
     
     
    listId = []
    for c in consultations:
        if not c.idPatient.id in listId:
            listId.append(c.idPatient.id)
            patientList2.append[p]
    
    for p in patients:
        if contain(patientList,p.FirstName,p.LastName,p.CNI_number) and p.id in listId:
            tmpList = []
            for a in patients:
                if a.FirstName == p.FirstName and a.LastName ==  p.LastName and a.CNI_number ==  p.CNI_number:
                    tmpList.append(a.id)
            patientList.append([p.FirstName,p.LastName,p.CNI_number,tmpList])
    
    
    context = {
        'consultationlist': consultations,
        'patientList': patientList,
        'selectName':name,
    }
    paginator = Paginator(patients, 5)
    page = request.GET.get('page')
    patients = paginator.get_page(page)
    patientList = []      
    return render(request, 'usermanagement/doctor/consultationlist.html',context=context)
        

def newconsultation(request):
    #traitement de la requete post
    if request.method == "POST":
        form1 =  ConsultationForm(request.POST).save()
        return consultationlist(request)
    else:   
        form1 = ConsultationForm()
    patientList = Patient.objects.filter(Service__iexact="generalist",status__iexact="valid")
    context = {
        'form':form1,
        'patientList':patientList,
        }
    return render(request, 'usermanagement/doctor/newconsultation.html', context=context)
    #objet formulaire sous forme d'un dictionnaire:{'form':form}

def newexamprescription(request):
    if request.method == "POST":
        ExamDescription = request.POST['ExamDescription'].split(',')
        for exam in ExamDescription:
                
            e = Examen() 
            e.idPatient = Patient.objects.filter(id__exact=request.POST['idPatient'])[0]
            e.status = 'invalid'
            e.pstatus = "invalid"
            e.Notes = request.POST['Notes']
            e.ExamCost = int(exam.split()[1])
            e.ExamDescription = exam.split()[0]
            e.save()
    form = ExamForm() 
    exams = Exam.objects.all()   
    patientList = Patient.objects.filter(Service__iexact="generalist",status__iexact="valid")
    context = {
        'form':form,
        'patientList':patientList,
        'exams':exams
        }
    return render(request, 'usermanagement/doctor/newexamprescription.html', context=context)


def examlist(request):
    def ndExam(idPatient):  
        m = Examen.objects.filter(idPatient__exact=idPatient,status__exact='invalid')
        print(idPatient)
        return len(m)
    
    name=""
    if request.method == 'POST':
        name = request.POST['name']
    
    examens = Examen.objects.all()
    listePatient = []
    for m in examens:
        if not m.idPatient in listePatient:
            if ndExam(m.idPatient.id)>0 and str(m.idPatient).__contains__(name):
                listePatient.append(m.idPatient)
    context = {
        'listePatient':listePatient,
        'examens':examens,
        'selectName':name,
    }
    return render(request=request,template_name='usermanagement/doctor/examlist.html',context=context)

def medecinelist(request):
    def ndMed(idPatient):
        m = Medicament.objects.filter(idPatient__exact=idPatient,status__exact='invalid')
        print(idPatient)
        return len(m)

    name=""
    if request.method == 'POST':
        name = request.POST['name']
    
    medicaments = Medicament.objects.all()
    listePatient = []
    for m in medicaments:
        if not m.idPatient in listePatient:
            if ndMed(m.idPatient.id)>0 and str(m.idPatient).__contains__(name):
                listePatient.append(m.idPatient)
    context = {
        'listePatient':listePatient,
        'medicaments':medicaments,
    }
    return render(request=request,template_name='usermanagement/doctor/medecinelist.html',context=context)


def newmedicineprescription(request):
    if request.method == "POST":
        MedicineName = request.POST['MedicineName'].split(',')
        for medicament in MedicineName:
            m = Medicament()
            m.idPatient = Patient.objects.filter(id__exact=request.POST['idPatient'])[0]
            m.status = 'invalid'
            m.pstatus = "invalid"
            m.Notes = request.POST['Notes']
            m.MedicineCost = int(medicament.split()[1])
            m.MedicineName = medicament.split()[0]
            m.save()     
         
    form = MedicineForm()
    drogs = Drog.objects.all()
    patientList = Patient.objects.filter(Service__iexact="generalist",status__iexact="valid")
    context = {
        'form':form,
        'patientList':patientList,
        'drogs':drogs,
        }
    return render(request, 'usermanagement/doctor/newmedicineprescription.html', context=context)  

def newexamprescription2(request,id):
    if request.method == "POST":
        ExamName = request.POST['ExamName'].split(',')
        for exam in ExamName:
                
            e = Examen() 
            e.idPatient = Patient.objects.filter(id__exact=request.POST['idPatient'])[0]
            e.status = 'invalid'
            e.pstatus = "invalid"
            e.Notes = request.POST['Notes']
            e.ExamCost = int(exam.split()[1])
            e.ExamDescription = exam.split()[0]
            e.save()
    form = ExamForm() 
    exams = Exam.objects.all()
    p = Patient.objects.filter(id__iexact=id)[0]
    patientList = Patient.objects.filter(Service__iexact="generalist",status__iexact="valid")
    context = {
        'form':form,
        'patientList':patientList,
        'patient':p,
        'exams':exams,
        }
    return render(request,'usermanagement/doctor/newexamprescription2.html',context=context)





def patientActions(request,id):
    p = Patient.objects.filter(id__iexact=id)[0]

    context={
        'id': id,
        'nom': p.FirstName,
    }
    return render(request,'usermanagement/doctor/patientActions.html',context=context)

def newconsultation2(request,id):
    #traitement de la requete post
    if request.method == "POST":
        form1 =  ConsultationForm(request.POST).save()
        return consultationlist(request)
    else:   
        form1 = ConsultationForm()
    patientList = Patient.objects.filter(Service__iexact="generalist",status__iexact="valid")
    p = Patient.objects.filter(id__iexact=id)[0]
    context = {
        'form':form1,
        'patientList':patientList,
        'patient': p,
        }
    return render(request,'usermanagement/doctor/newconsultation2.html',context=context)




def newmedicineprescription2(request,id):

    if request.method == "POST":
        MedicineName = request.POST['MedicineName'].split(',')
        for medicament in MedicineName:
            m = Medicament()
            m.idPatient = Patient.objects.filter(id__exact=request.POST['idPatient'])[0]
            m.status = 'invalid'
            m.pstatus = "invalid"
            m.Notes = request.POST['Notes']
            m.MedicineCost = int(medicament.split()[1])
            m.MedicineName = medicament.split()[0]
            m.save()
    form = MedicineForm()
    p = Patient.objects.filter(id__iexact=id)[0]
    drogs = Drog.objects.all()
    patientList = Patient.objects.filter(Service__iexact="generalist",status__iexact="valid")
    context = {
        'form':form,
        'patientList':patientList,
        'drogs':drogs,
        'patient':p,
        }
    return render(request,'usermanagement/doctor/newmedicineprescription2.html',context=context)






#---------------------------------------PHARMACIST---------------------------------------------#
#---------------------------------------PHARMACIST---------------------------------------------#
#---------------------------------------PHARMACIST---------------------------------------------#


def pharmacist(request):        
    return render(request, 'usermanagement/pharmacist/pharmacist.html')

def facturemedicament(request,id):
    if request.method== 'POST':
        listeMed = Medicament.objects.filter(idPatient__exact=id)
        coast = 0
        validMed = []
        for m in listeMed:
            if str(m.id) in request.POST:
                if request.POST[str(m.id)] == 'valid':
                    validMed.append(m)
                    coast +=  m.MedicineCost
                    m.status = 'valid'
                    m.save()
        nom = Patient.objects.filter(id__exact=id)[0]
        d = datetime.now()
        context = {'validMed':validMed,'nom':nom, 'coast': coast,'d':d}
        return render(request, 'usermanagement/pharmacist/facturemedicament.html',context)
    return pharmacistviewpl(request)

def pharmacistviewpl(request):
    def ndMed(idPatient):
        m = Medicament.objects.filter(idPatient__exact=idPatient,status__exact='invalid')
        print(idPatient)
        return len(m)
    medicaments = Medicament.objects.all()
    listePatient = []
    for m in medicaments:
        if not m.idPatient in listePatient:
            if ndMed(m.idPatient.id)>0:
                listePatient.append(m.idPatient)
    context = {
        'listePatient':listePatient,
        'medicaments':medicaments,
    }
    return render(request=request,template_name='usermanagement/pharmacist/pharmacistviewpl.html',context=context)


    
#---------------------------------------LAB_TECHNICIAN---------------------------------------------#
#---------------------------------------LAB_TECHNICIAN---------------------------------------------#
#---------------------------------------LAB_TECHNICIAN---------------------------------------------#


def labtechviewpl(request):
    def ndExam(idPatient):
        # patients = Patient.objects.filter(FirstName__contains=name).order_by("Date")[::-1]
        m = Examen.objects.filter(idPatient__exact=idPatient,pstatus__exact="valid",status__exact='invalid')
        # print(idPatient)
        return len(m)
    examens = Examen.objects.all()
    
    name = ''
    if request.method == 'POST':
        if 'name' in request.POST:
            name = request.POST['name']
    listePatient = []

    # listePatient = []
    for m in examens:
        if not m.idPatient in listePatient and m.pstatus == 'valid':
            if ndExam(m.idPatient.id)>0:
                listePatient.append(m.idPatient)
    context = {
        'listePatient':listePatient,
        'examens':examens,
        # 'patients':patients,
    }
    return render(request=request,template_name='usermanagement/labTechnician/labtechviewpl.html',context=context)


def factureexamen(request,id):
    if request.method== 'POST':
        listeExamen = Examen.objects.filter(idPatient__exact=id)
        validExam = []
        cost = []
        for m in listeExamen:
            if str(m.id) in request.POST:
                if request.POST[str(m.id)] == 'valid':
                    validExam.append(m)
                    m.status = 'valid'
                    m.save()
        nom = Patient.objects.filter(id__exact=id)[0]
        context = {'validExam':validExam,'nom':nom}
        return render(request, 'usermanagement/labTechnician/factureexamen.html',context)
    return labtechviewpl(request)


#---------------------------------------CASHIER---------------------------------------------#
#---------------------------------------CASHIER---------------------------------------------#
#---------------------------------------CASHIER---------------------------------------------#
#---------------------------------------CASHIER---------------------------------------------#


def cashierviewpl(request):
    medicament_list = Medicament.objects.all()
    examen_list = Examen.objects.all()

    listePatient = []
    for m in medicament_list:
        if not m.idPatient in listePatient and m.status == 'valid': 
            listePatient.append(m.idPatient)

    for m in examen_list:
        if not m.idPatient in listePatient and m.status == 'valid':
            listePatient.append(m.idPatient)


    context = {"listePatient":listePatient,"examen_list":examen_list,"medicament_list":medicament_list}
    return render(request, 'usermanagement/cashier/cashierviewpl.html',context=context)
    

def viewbill(request,idPatient):
    nom = Patient.objects.filter(id__exact=idPatient)[0]
    medicament_list = Medicament.objects.filter(idPatient__exact=idPatient)
    examen_list = Examen.objects.filter(idPatient__exact=idPatient)

    coast = 0
    validMed = []
    for m in medicament_list:
        if not m in validMed and m.status == 'valid' and m.idPatient.id == int(idPatient): 
            validMed.append(m)
            coast += m.MedicineCost
    validExam = []
    for m in examen_list:
        if not m in validExam and m.status == 'valid' and m.idPatient.id == int(idPatient):
            validExam.append(m) 
            coast += m.ExamCost
    context={
        "validMed":validMed,
        "validExam":validExam,
        "nom":nom,
        "coast":coast
        }
    return render(request,'usermanagement/cashier/viewbill.html',context=context)

def viewconsultationlist(request):
    name = ''
    if request.method == 'POST':
        if 'name' in request.POST:
            name = request.POST['name']
    patientList = Patient.objects.filter(status__iexact='invalid',FirstName__contains=name).order_by("Date")[::-1]
    context = {
        'patientList':patientList,
    }
    return render(request=request,template_name='usermanagement/cashier/viewconsultationlist.html',context=context)

def validation(request, id):
    p = Patient.objects.filter(id__exact=id)
    context = {}
    if not p is None:
        context={
            "p": p[0]
        }
    return render(request,'usermanagement/cashier/validation.html',context=context)
     

def savevalidation(request,id):
    p = Patient.objects.filter(id__exact=id)[0]
    p.status = "valid"
    p.save()
    return viewconsultationlist(request)

def cashierviewexam(request):
    name = ''
    if request.method == 'POST':
        if 'name' in request.POST:
            name = request.POST['name']   #Il faut la jointure pour filtrer selon le nom
    patientList = Patient.objects.filter(FirstName__contains=name)
    examList = Examen.objects.filter(pstatus__exact='invalid').order_by("Date")[::-1]
    
    context = {
        'examList':examList,
        # 'patientList':patientList,
    }
    return render(request=request,template_name='usermanagement/cashier/cashierviewexam.html',context=context)

def validationexams(request, id):
    p = Examen.objects.filter(id__exact=id)
    context = {}
    if not p is None:
        context={
            "p": p[0]
        }
    return render(request,'usermanagement/cashier/validationexams.html',context=context)


def savevalidationexams(request,id):
    try:
        e = Examen.objects.filter(id__exact=id)[0]
        e.pstatus = "valid"
        e.save()
    except:
        pass
    return cashierviewexam(request)

def consultationbill(request, id):
    context = {}
    p = Patient.objects.filter(id__exact=id)[0]
    p.status = "valid"
    p.save()
    if not p is None:
        context={
            "p": p
        }
    return render(request,'usermanagement/cashier/consultationbill.html',context=context)


def cashierhistory(request):
    name = ''
    if request.method == 'POST':
        if 'name' in request.POST:
            name = request.POST['name']
    patientList = Patient.objects.filter(status__exact='valid', FirstName__contains=name).order_by("Date")[::-1]
    context = {
        'patientList':patientList,
    }
    return render(request,'usermanagement/cashier/cashierhistory.html', context=context)


def examshistory(request):
    name = ''
    if request.method == 'POST':
        if 'name' in request.POST:
            name = request.POST['name']  #Il faut la jointure pour filtrer selon le nom
    examList = Examen.objects.filter(pstatus__exact='valid').order_by("Date")[::-1]
    context = {
        'examList':examList,
    }
    return render(request=request,template_name='usermanagement/cashier/examshistory.html',context=context)

     




#---------------------------------------DENTIST---------------------------------------------#
#---------------------------------------DENTIST---------------------------------------------#
#---------------------------------------DENTIST---------------------------------------------#
#---------------------------------------DENTIST---------------------------------------------#
#---------------------------------------DENTIST---------------------------------------------#
#---------------------------------------DENTIST---------------------------------------------#

# def dentistviewpl(request):
#     return render(request, 'usermanagement/dentist/dentistviewpl.html')

def sendToGeneralistValidation(request, id):
    p = Patient.objects.filter(id__exact=id)[0]
    context={
            "p": p
        }     
    return render(request, 'usermanagement/dentist/sendToGeneralistValidation.html', context=context)



def sendToGeneralist(request, id):
    p = Patient.objects.filter(id__iexact=id)[0]
    p.sentStatus = "notSent"
    p.Service = "generalist"
    p.save()
    context={
        "p":p
    }
    return render(request, 'usermanagement/dentist/sendToGeneralist.html', context=context)

def dentistviewpl(request):
    if request.method == 'POST':
        name = ''
        if 'name' in request.POST:
            name = request.POST['name']
        patients = Patient.objects.filter(FirstName__contains=name,Service__iexact="specialist",status__iexact="valid")
        patientList = []
        
        for p in patients:
            if not [p.FirstName,p.LastName,p.CNI_number] in patientList:
                patientList.append([p.FirstName,p.LastName,p.CNI_number]) 
        context = {
            'patientList':patientList,
            'patients': patients,
            'selectName':name,
        }
        return render(request, 'usermanagement/dentist/dentistviewpl.html', context)
    patients = Patient.objects.filter(Service__iexact="specialist",status__iexact="valid")
    patientList = []
    for p in patients:
        if not [p.FirstName,p.LastName,p.CNI_number] in patientList:
            patientList.append([p.FirstName,p.LastName,p.CNI_number])
    context = {
        'patientList':patientList,
        'patients': patients,
    }
    return render(request, 'usermanagement/dentist/dentistviewpl.html', context)


class DoctorPatientDeleteView(DeleteView):
    model = Patient
    success_url = reverse_lazy('usermanagement:doctorviewpl')


def consultationlist(request):
    def contain(patientList,nom,prenom,cni):
        for n,p,c,l in patientList:
            if n==nom and p == prenom and c == cni:
                return False
        return True
    name = ''
    if request.method == 'POST':
        if 'name' in request.POST:
            name = request.POST['name']
    patientList = []
    patients = Patient.objects.filter(FirstName__contains = name)
    listId = []
    for p in patients:
        listId.append(p.id) 

    consultations = Consultation.objects.filter(idPatient__in=listId)
    listId = []
    for c in consultations:
        if not c.idPatient.id in listId:
            listId.append(c.idPatient.id)
    
    for p in patients:
        if contain(patientList,p.FirstName,p.LastName,p.CNI_number) and p.id in listId:
            tmpList = []
            for a in patients:
                if a.FirstName == p.FirstName and a.LastName ==  p.LastName and a.CNI_number ==  p.CNI_number:
                    tmpList.append(a.id)
            patientList.append([p.FirstName,p.LastName,p.CNI_number,tmpList])
    context = {
        'consultationlist': consultations,
        'patientList': patientList,
        'selectName':name,
    }
    return render(request, 'usermanagement/doctor/consultationlist.html',context=context)
 
def dconsultationlist(request):
    def contain(patientList,nom,prenom,cni):
        for n,p,c,l in patientList:
            if n==nom and p == prenom and c == cni:
                return False
        return True
    name = ''
    if request.method == 'POST':
        if 'name' in request.POST:
            name = request.POST['name']
    patientList = []
    patients = Patient.objects.filter(FirstName__contains = name)
    listId = []
    for p in patients:
        listId.append(p.id) 

    consultations = Consultation.objects.filter(idPatient__in=listId)
    listId = []
    for c in consultations:
        if not c.idPatient.id in listId:
            listId.append(c.idPatient.id)
    
    for p in patients:
        if contain(patientList,p.FirstName,p.LastName,p.CNI_number) and p.id in listId:
            tmpList = []
            for a in patients:
                if a.FirstName == p.FirstName and a.LastName ==  p.LastName and a.CNI_number ==  p.CNI_number:
                    tmpList.append(a.id)
            patientList.append([p.FirstName,p.LastName,p.CNI_number,tmpList])
    context = {
        'consultationlist': consultations,
        'patientList': patientList,
        'selectName':name,
    }
    return render(request, 'usermanagement/dentist/dconsultationlist.html',context=context)

   
def dnewconsultation(request):
    if request.method == "POST":

        form1 =  ConsultationForm(request.POST).save()
        return consultationlist(request)
    else:   
        form1 = ConsultationForm()
        patientList = Patient.objects.filter(Service__iexact="specialist",status__iexact="valid")
        context = {
            'form':form1,
            'patientList':patientList,
        }
    return render(request, 'usermanagement/dentist/dnewconsultation.html', context=context)
       
   

    #objet formulaire sous forme d'un dictionnaire:{'form':form}

def dexamlist(request):
    def ndExam(idPatient):
        m = Examen.objects.filter(idPatient__exact=idPatient,status__exact='invalid')
        print(idPatient)
        return len(m)
    
    name=""
    if request.method == 'POST':
        name = request.POST['name']
    
    examens = Examen.objects.all()
    listePatient = []
    for m in examens:
        if not m.idPatient in listePatient:
            if ndExam(m.idPatient.id)>0 and str(m.idPatient).__contains__(name):
                listePatient.append(m.idPatient)
    context = {
        'listePatient':listePatient,
        'examens':examens,
        'selectName':name,
    }
    return render(request=request,template_name='usermanagement/dentist/dexamlist.html',context=context)


def dnewexamprescription(request):
    if request.method == "POST":
        form =  ExamForm(request.POST)
        form = ExamForm()    

        return render(request, 'usermanagement/dentist/dnewexamprescription.html', {'form':form})
    else:   
        form = ExamForm()
        patientList = Patient.objects.filter(Service__iexact="specialist",status__iexact="valid")
    context = {
        'form':form,
        'patientList':patientList,
        }

    return render(request, 'usermanagement/dentist/dnewexamprescription.html', context=context)



def dmedecinelist(request):
    def ndMed(idPatient):
        m = Medicament.objects.filter(idPatient__exact=idPatient,status__exact='invalid')
        print(idPatient)
        return len(m)

    name=""
    if request.method == 'POST':
        name = request.POST['name']
    
    medicaments = Medicament.objects.all()
    listePatient = []
    for m in medicaments:
        if not m.idPatient in listePatient:
            if ndMed(m.idPatient.id)>0 and str(m.idPatient).__contains__(name):
                listePatient.append(m.idPatient)
    context = {
        'listePatient':listePatient,
        'medicaments':medicaments,
    }
    return render(request=request,template_name='usermanagement/dentist/dmedecinelist.html',context=context)

def dnewmedecineprescription(request):
    if request.method == "POST":
        form =  MedicineForm(request.POST).save()
        form = MedicineForm()  
        return render(request, 'usermanagement/dentist/dnewmedecineprescription.html', {'form':form})
        
    else:   
        form = MedicineForm()
        patientList = Patient.objects.filter(Service__iexact="specialist",status__iexact="valid")
    context = {
        'form':form,
        'patientList':patientList,
        }   
    return render(request, 'usermanagement/dentist/dnewmedecineprescription.html', context=context)

