
from django.shortcuts import render,redirect,HttpResponse
# from .forms import usersignup
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
from .models import student_register
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

from django.conf import settings
import pyrebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import auth



firebaseConfig = {
  "apiKey": "AIzaSyB3oat-wcH0z45mC7wJoXSTV_Qr60GKmv0",
  "authDomain": "extech-d485a.firebaseapp.com",
  "databaseURL": "https://extech-d485a-default-rtdb.firebaseio.com",
  "projectId": "extech-d485a",
  "storageBucket": "extech-d485a.appspot.com",
  "messagingSenderId": "254602568072",

}
cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred)


def signup(request):
    if request.user.is_authenticated:

        return redirect('dashbord')
    else:
        if request.method=='POST':
            first_name=request.POST['first_name']
            mobile_no=request.POST['mobile_no']
            email=request.POST['email'] 
            username=request.POST['username']
            password=request.POST['password']
            if User.objects.filter(last_name=mobile_no).exists():
                messages.error(request,"Mobile no is already exists")
                return render(request,"registration2.html")
            elif User.objects.filter(email=email).exists():
                messages.error(request,'Email is aleready in use !')
                return render(request,'registration2.html')

            elif User.objects.filter(username=username).exists():
                messages.error(request,'Username is aleready in use !')
                return render(request,'registration2.html')
                
          
            else:
                user=auth.create_user(email=email,password=password,phone_number=mobile_no)
                data=User.objects.create_user(first_name=first_name,last_name=mobile_no,email=email,username=username,password=password)
                    
                data.save() 
                messages.success(request,'register sucessfully')
                return redirect('signup')
        else:
            return render(request,'registration2.html')

def login_user(request):
    if request.user.is_authenticated:
        return redirect('dashbord')
    else:
        if request.method=='POST':
            username = request.POST['username']
            password = request.POST['password']
            user =authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                messages.success(request,' welcome '+ username)
                return redirect ('dashbord')
            else:
                messages.error(request,' Invalid username password!')
                return redirect('login')
        else:   
            return render(request,'login.html')

@login_required(login_url='login')
def main(request):
    if request.method=="POST":
        data=student_register(request.POST)
        id=request.POST['id']
        first_name=request.POST['first_name'] 
        last_name=request.POST['last_name']
        fathername=request.POST['fathername']
        starts_on=request.POST['starts_on']
        ends_on=request.POST['ends_on']
        if starts_on>ends_on:
            data=student_register(id=id,first_name=first_name,last_name=last_name,fathername=fathername,starts_on=starts_on,ends_on=ends_on)
            data.save()
            messages.info(request,' Data Added Sucessfully')
            return redirect('main')
        else:
            messages.error(request,'Invalid Date')
            return redirect('main')
    else:
        
        return render (request,'admin.html')

@login_required(login_url='login')
def dashbord(request):
    alldata=student_register.objects.all()
    return render(request,'dashbord.html',{'alldata':alldata})

@login_required(login_url='login')
def delete_data(request,id):
    if request.method=="POST":
        alldata=student_register.objects.get(pk=id)
        alldata.delete()
        messages.info(request,' Data deleted Sucessfully')
        return redirect('dashbord')

@login_required(login_url='login')
def edit_data(request,id):
    data=student_register.objects.get(id=id)
    return render(request,'student-edit.html',{'data':data})

@login_required(login_url='login')
def update(request, id):
    if request.method=="POST":
        id=request.POST.get('id')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        fathername=request.POST.get('fathername')
        starts_on=request.POST.get('starts_on')
        ends_on=request.POST.get('ends_on')
        if starts_on>ends_on:
            data=student_register(id=id,first_name=first_name ,last_name=last_name,fathername=fathername,starts_on=starts_on,ends_on=ends_on)
            data.save()
            messages.success(request,' Data updated Sucessfully')
            return redirect('dashbord')
        else:
            messages.error(request,'Invalid Date')
            return redirect('update')
    return render(request,'student-edit.html')

@login_required(login_url='login')
def logout_user(request):
    logout(request)
    messages.info(request,' Logout Sucessfully')
    return redirect('login')
    

        