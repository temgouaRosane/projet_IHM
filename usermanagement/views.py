from django.shortcuts import redirect, render
from django.views.generic.edit import UpdateView, DeleteView
from usermanagement.models import Patient
from .formulaire import  PatientForm
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    return render(request, 'usermanagement/index.html')

def home(request):
    if request.user.role == "Receptionist":
        return render(request, 'usermanagement/receptionist.html')
    return render(request, 'usermanagement/home.html')

def reception(request):
     return render(request, 'usermanagement/reception.html')

def about(request):
    return render(request, 'usermanagement/about.html')

def pharmacy(request):
    return render(request, 'usermanagement/pharmacy.html')


def addPatient(request):
    #traitement de la requete post
    if request.method == "POST":
        form = PatientForm(request.POST).save()
        return redirect('/addPatient')
    else:   
        form = PatientForm()
    
    return render(request, 'usermanagement/addPatient.html', {'form':form})

#objet formulaire sous forme d'un dictionnaire:{'form':form}






def viewpatientlist(request):
    if request.method == 'POST':
        name = request.POST['name']
        patients = Patient.objects.filter(FirstName__contains=name)
        context = {
            'patients': patients,
            'selectName':name,
        }
        return render(request, 'usermanagement/viewpatientlist.html',context=context)
        pass
    patients = Patient.objects.all()
    context = {
        'patients': patients,
    }
    return render(request, 'usermanagement/viewpatientlist.html', context)


class PatientUpdateView(UpdateView):
    model = Patient
    fields = '__all__'
    template_name_suffix = '_update_form'

class PatientDeleteView(DeleteView):
    model = Patient
    success_url = reverse_lazy('usermanagement:viewpatientlist')