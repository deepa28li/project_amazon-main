from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse,HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse


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
                      'deepalipatil2800@gmail.com',
                      [NSUFO.email],
                      fail_silently=False )
            return HttpResponse('registration form is successful check in admin')        
    return render(request,'registration.html',d)



# ------------------home page------------------

def home(request):
    if request.session.get('username'):
        username=request.session.get('username')
        d={'username':username}
        return render(request,'home.html',d)
    return render(request,'home.html')

# --------------login page------------------

def user_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        AUO=authenticate(username=username,password=password)
        if AUO:
            if AUO.is_active:
                login(request,AUO)
                request.session['username']=username
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse('Not a Active User')
        else:
            return HttpResponse('Invalid Details')
    return render(request,'user_login.html')

# ---------------reset password ----------------

def reset_password(request):
    if request.method=='POST':
        password=request.POST['pw']
        username=request.POST['un']
        LUO=User.objects.filter(username=username)
        if LUO:
            UO=LUO[0]
            UO.set_password(password)
            UO.save()
            return HttpResponse('reset_password is done')
        else:
            return HttpResponse('invalid data')
    return render(request,'reset_password.html')

# -------------logout------------------

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))