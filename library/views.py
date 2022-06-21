
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from library.forms import addbookform, loginform, signupform
from django.contrib.auth import authenticate,login,logout
from library.models import books
from django.contrib.auth.models import User
# Create your views here.

def home(requests):
    return render(requests,'library/home.html')


#signup
def usersignup(requests):

    if requests.method=='POST':
        fm = signupform(requests.POST)
        if fm.is_valid():
            fm.save()
            messages.success(requests,"Account created successfully!!")
            return HttpResponseRedirect('/login/')
    else:        
        fm = signupform()
    return render(requests,'library/signup.html',{'fm':fm})


def userlogin(requests):
    if not requests.user.is_authenticated:
        if requests.method == "POST":
            fm = loginform(request = requests,data = requests.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname,password = upass)
                if user is not None:
                    login(requests,user)
                    messages.success(requests,"Loggedin successfully!!")
                    return HttpResponseRedirect('/profile/')
            else:
               messages.success(requests,"User Does Not Exit. Please Signup first.")
        else:
            fm  = loginform()
        return render(requests,'library/login.html',{'fm':fm})
    else:
        return HttpResponseRedirect('/profile/')

def userprofile(requests):
    if requests.user.is_authenticated:
        book = books.objects.all()
        us = requests.user
        
        return render(requests,'library/profile.html',{'book':book,'user':us})
    else:
        return HttpResponseRedirect('/login/')

def userlogout(requests):
    logout(requests)
    return HttpResponseRedirect('/')

def addbook(requests):
    if requests.user.is_authenticated:
        if requests.method=='POST':
            fm  = addbookform(requests.POST)
            fm.is_valid()
            fm.save()
            messages.success(requests,"Book Added Successfully!!")
            return HttpResponseRedirect('/profile/')
        else:
            fm = addbookform()
        return render(requests,'library/addbook.html',{'fm':fm})
    else:
        return HttpResponseRedirect('/login')


def updatebook(requests,id):
    if requests.user.is_authenticated:
        bk = books.objects.get(pk=id)
        if requests.method =='POST':
            fm = addbookform(requests.POST,instance = bk)
            if fm.is_valid():
                fm.save()
                messages.success(requests,"Book Update Successfully..")
                return HttpResponseRedirect('/profile/')
        else:
            fm = addbookform(instance = bk)
        return render(requests,'library/updatebook.html',{'fm':fm})
    else:
        return HttpResponseRedirect('/login/')


def guests(requests):
    if not requests.user.is_authenticated:
        book = books.objects.all()
        return render(requests,'library/profile.html',{'book':book})

