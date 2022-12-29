from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import BookDatabase
from .forms import DatabaseForm

about = [
    {'id':1, 'name': 'How this got started'},
    {'id':2, 'name': 'Who is this program for'},
    {'id':3, 'name': 'Why it is important'},
] 

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get(username)
        password = request.POST.get(password)

        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request, 'User does not exist')
        
            user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or Password is incorrect')

    context = {}
    return render(request, 'base/login_register.html', context)

def home(request):
    databases = BookDatabase.objects.all()
    context = {'databases': databases }
    return render(request, 'base/home.html', context)

def database(request, pk):
    databases = BookDatabase.objects.all()
    context = {'database': database}
    return render(request, 'base/database.html', context)

def aboutpage(request, pk):
    aboutpage = None

    for i in about:
        if i['id'] == int(pk):
            aboutpage = i

    context = {'aboutpage': aboutpage}    
    return render(request,'base/about.html', context)

def databaseForm(request):
    databases = BookDatabase.objects.all()
    row_count = databases.count()
    form = DatabaseForm()

    if request.method == 'POST':
        form = DatabaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('database-form')

    context = {'form':form,'databases':databases, 'row_count':row_count}
    return render(request, 'base/database_form.html', context)