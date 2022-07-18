from cmath import log
from operator import is_not
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Detail
from .forms import DetailForm, CreateUserForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    if request.method == 'POST':
        form = DetailForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = DetailForm()

    context = {
        'form': form,
        'details': Detail.objects.all()
    }
    return render(request, 'add.html', context)

@login_required
def delete( request , del_id):
    if request.method == 'POST':
         data = Detail.objects.get(pk=del_id)
         data.delete()
         return redirect('index')

@login_required
def update(request,del_id):
    if request.method == 'POST':
        pi=Detail.objects.get(pk=del_id)
        form = DetailForm(request.POST,request.FILES,instance=pi)
        if form.is_valid():
            form.save()
    else:
            pi=Detail.objects.get(pk=del_id)
            form = DetailForm(instance=pi)
    return render(request, 'update.html',{'form':form})

def register(request):
    if request.method == 'POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_page')
    else:
        form=CreateUserForm()
    context={'form':form}
    return render(request,'register.html',context)
    
def login_page(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('index')

    return render(request,'login.html')
        
    
   
   
