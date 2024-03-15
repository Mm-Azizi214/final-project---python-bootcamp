from django.shortcuts import render, redirect
from final.reg_form import RegisterForm
from django.contrib.auth import authenticate, login
from final.login import LoginForm
from final.models import Criticism
from final.Criticism_Form import Criticism_Form ,Criticism_update_Form

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('menu')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def home(request):
    return render(request,"home.html")

def menu(request):
    return render(request,"menu.html")

def criticismm(request,criticism_id):
    criticism1=Criticism.objects.get(id=criticism_id)
    return render(request ,"criticismm.html",{"criticismm":criticism1})

def criticism_list(request):
    criticism_list=Criticism.objects.all()
    return render(request , "criticism_list.html",{"context":criticism_list})

def create_criticism(request):
    if request.method == 'POST':
        form=Criticism_Form(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            Criticism.objects.create(moive_name=cd['moive_name'],body=cd['body'],created=cd['created'])
            return redirect('menu')
    else:
        form= Criticism_Form()
    return render (request,"write_criticism.html",{"form":form})
    
def delete(request,criticism_id):
    Criticism.objects.get(id=criticism_id).delete()
    return redirect("criticism_list")

def update(request,criticism_id):
    criticism1=Criticism.objects.get(id=criticism_id)
    if request.method == 'POST':
        form=Criticism_update_Form(request.POST,instance=criticism1)
        if form.is_valid():
            form.save()
            return redirect("criticism_list")
    else:
        form= Criticism_update_Form(instance=criticism1)
    return render (request,"update.html",{"form":form})