from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse,HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login



# ----------registration-------------
def registration(request):
    d={'usfo':UserForm(),'pfo':ProfileForm()}
    if request.method=='POST' and request.FILES:
        usfd=UserForm(request.POST)
        pfd=ProfileForm(request.POST,request.FILES)
        if usfd.is_valid() and pfd.is_valid():
            NSUFO=usfd.save(commit=False)
            submittedPassword=usfd.cleaned_data['password']
            NSUFO.set_password(submittedPassword)
            NSUFO.save()
            NSPO=pfd.save(commit=False)
            NSPO.username=NSUFO
            NSPO.save()
            
            
            send_mail('registartion',
                      'registration is sucessful in amazon ',
                      'oppalanaveen143@gmail.com',
                      [NSUFO.email],
                      fail_silently=False )
            return HttpResponse('registration form is successful check in admin')        
    return render(request,'registration.html',d)
