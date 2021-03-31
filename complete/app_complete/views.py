from django.shortcuts import render,redirect
from app_complete.forms import UserForm,ProfileForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import login,logout,authenticate

def index(request):
    return render(request,'app_complete/index.html')

def register(request):
    registered=False
    if request.method=='POST':
        user_form=UserForm(data=request.POST)
        profile_form=ProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.save()

            profile=profile_form.save(commit=False)
            profile.user=user
            if 'profile_pic' in request.FILES:
                profile.profile_pic=request.FILES['profile_pic']
            profile.save()
            registered=True
        else:
            print('error find')
    else:
        user_form=UserForm()
        profile_form=ProfileForm()

    return render(request,'app_complete/registration.html',{'user_form':user_form,
                                                            'profile_form':profile_form,
                                                            'registered':registered})

def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect(reverse('index'))
            else:
                return HttpResponse('account is not active')
        else:
            return HttpResponse("some one tried to accesur page")
    else:
        return render(request,'app_complete/login.html',{})

@login_required
def user_logout(request):
    logout(request)
    return redirect('index')

