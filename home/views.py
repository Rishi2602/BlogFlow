from cmath import log
from operator import is_not
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Detail,Profile
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User


@login_required
def add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        completion = request.POST.get('completion')
        if completion=="on":
            completion=True
        else:
            completion=False
        form=Detail(users=request.user,title=title,description=description,completion=completion)
        form.save()
        messages.success(request,'Your Todo has been added')
    return render(request,'add.html')

@login_required
def index(request):
    user_details=request.user
    context={
        'details':Detail.objects.filter(users=user_details,completion=False),
        'user_details':user_details,
    }
    return render(request,'info.html',context)

@login_required
def profile(request):
    user_details=request.user
    context={
        'user_details':user_details,
        'profile':Profile.objects.filter(user=user_details)
    }
    return render(request,'profile.html',context)

@login_required
def colist(request):
    user_details=request.user
    context={
        'details':Detail.objects.filter(users=user_details,completion=True),
        'user_details':user_details
    }
    return render(request,'colist.html',context)


@login_required
def delete(request,del_id):
    if request.method == 'POST':
         data = Detail.objects.get(pk=del_id)
         data.delete()
         messages.success(request,'Your Todo has been deleted.')
    context={
        'details':Detail.objects.filter(completion=False),
    }
    return render(request,'info.html',context)

        

@login_required
def update(request,del_id):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        completion = request.POST.get('completion')
        if completion==None:
            completion=False
        else:
            completion=True
        form=Detail(id=del_id,users=request.user,title=title,description=description,completion=completion)
        form.save()
        messages.success(request,'Updated successfully!')
    return render(request, 'update.html',{
        'details':Detail.objects.filter(id=del_id)})

def register(request):
    if request.method == 'POST':
        username=request.POST.get('username1')
        email=request.POST.get('email')
        number=request.POST.get('number')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        image=request.FILES.get('image')
        user=User.objects.create_user(username, email, pass1)
        user.save()
        profile=Profile(user=user,PhoneNumber=number,ProfilePicture=image)
        profile.save()
        messages.success(request,'Account created successfully!')

    return render(request,'register.html')
    
def login_page(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')

    return render(request,'login.html')

@login_required        
def logoutUser(request):
    logout(request)
    return redirect('login_page')    
   
   
