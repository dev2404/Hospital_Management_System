from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from myapp.models import Appointment
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import *


# Create your views here.

def index(request):
    return render(request, "index.html")
    #return HttpResponse("this is home page")


def contact(request):
    return render(request, "contact.html")     

def facilities(request):
    return render(request, "facilities.html")

def login1(request):
    if request.method=='POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)

        if user is not None:
            #a backend authenticated the crendentials
            login(request, user)
            return redirect("index1")
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')


def index1(request):
    if request.user.is_anonymous:
        return redirect("/login")
    doctor = Doctor.objects.all()
    patient = Patient.objects.all()
    appointment1 = Appointment1.objects.all()


    d = 0
    p = 0
    a = 0
    for i in doctor:
        d+=1
    for i in patient:
        p+=1
    for i in appointment1:
        a+=1     
    d1 = {'d':d, 'p':p, 'a':a}       

    return render(request, "index1.html", d1)  
    



def appointment(request):
    #return HttpResponse("this is facilities page")
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        desc = request.POST.get('desc')
        appointment = Appointment(name=name, email=email, phone=phone, address=address, desc=desc, date= datetime.today())
        appointment.save()
        messages.success(request, 'your time of appointment have been taken.')


    return render(request, 'appointment.html')                  
                      
  
def view_doctor(request):
    doc = Doctor.objects.all()  
    d = {'doc':doc}  
    return render(request, 'view_doctor.html', d)  

def Add_Doctor(request):
    error=""
    if request.method=='POST':
        n = request.POST['name']
        c = request.POST['contact']
        sp = request.POST['special']
        try:
            Doctor.objects.create(name=n, phone=c, special=sp)
            error="no"
        except:
            error="yes"
    d = {'error':error}
    return render(request, 'add_doctors.html', d)            

def Delete_Doctor(request, pid):
    doctor = Doctor.objects.get(id=pid)
    doctor.delete()
    return redirect('view_doctor')

def view_patient(request):
    pat = Patient.objects.all()  
    d = {'pat':pat}  
    return render(request, 'view_patient.html', d)  

def Add_Patient(request):
    error=""
    if request.method=='POST':
        n = request.POST['name']
        g = request.POST['gender']
        m = request.POST['phone']
        a = request.POST['address']
        try:
            Patient.objects.create(name=n, gender=g, phone=m, address=a)
            error="no"
        except:
            error="yes"
    d = {'error':error}
    return render(request, 'add_patient.html', d)            

def Delete_Patient(request, pid):
    patient = Patient.objects.get(id=pid)
    patient.delete()
    return redirect('view_patient')

def view_appointment(request):
    appoint = Appointment1.objects.all()  
    d = {'appoint':appoint}  
    return render(request, 'view_appointment.html', d)  

def Add_Appointment(request):
    error=""
    doctor1 = Doctor.objects.all()
    patient1 = Patient.objects.all()

    if request.method=='POST':
        d = request.POST['doctor']
        p = request.POST['patient']
        d1 = request.POST['date']
        t1 = request.POST['time']
        doctor = Doctor.objects.filter(name=d).first()
        patient = Patient.objects.filter(name=p).first()

        try:
            Appointment1.objects.create(doctor=doctor, patient=patient, date=d1, time=t1)
            error="no"
        except:
            error="yes"
    d = {'doctor':doctor1, 'patient':patient1, 'error':error}
    return render(request, 'add_appointment.html', d)            

def Delete_Appointment(request, pid):
    appointment = Appointment1.objects.get(id=pid)
    appointment.delete()
    return redirect('view_appointment')
