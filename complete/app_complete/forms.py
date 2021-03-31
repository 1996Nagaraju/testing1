from django import forms
from django.contrib.auth.models import User
from app_complete.models import profileinfo

class UserForm(forms.ModelForm):
    class Meta():
        model=User
        fields=('username','password','email')

class ProfileForm(forms.ModelForm):
    class Meta():
        model=profileinfo
        fields=('portfolio','profile_pic')

