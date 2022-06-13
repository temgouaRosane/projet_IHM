from django.shortcuts import render

def login(request):
    
    context = {}
    return render(request,template_name='account/login.html',context=context)

def redirection(request):
    if request.method == 'POST':
        pass
    context = {}
    return render(request,template_name='account/login.html',context=context)