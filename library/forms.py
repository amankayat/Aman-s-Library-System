from cProfile import label
from dataclasses import field
from turtle import width
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django import forms
from django.contrib.auth.models import User

from library.models import books
class signupform(UserCreationForm):
    password1= forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ("username","first_name","last_name","email")
        widgets = {"username":forms.TextInput(attrs={'class':'form-control'}),
        "first_name":forms.TextInput(attrs={'class':'form-control'}),
        "last_name":forms.TextInput(attrs={'class':'form-control'}),
        "email":forms.TextInput(attrs={'class':'form-control'})
        }

class loginform(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))


class addbookform(forms.ModelForm):

    class Meta:
        model = books
        fields = ("name","subject","author","publish")
        widgets = {"name":forms.TextInput(attrs={'class':'form-control'}),
        "subject":forms.TextInput(attrs={'class':'form-control'}),
        "author":forms.TextInput(attrs={'class':'form-control'}),
        "publish":forms.DateInput(attrs={'type':'date','class':'form-control'}),
        }
        

