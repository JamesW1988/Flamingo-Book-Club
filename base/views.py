from django.shortcuts import render, redirect
from .models import BookDatabase
from .forms import DatabaseForm


about = [
    {'id':1, 'name': 'How this got started'},
    {'id':2, 'name': 'Who is this program for'},
    {'id':3, 'name': 'Why it is important'},
] 

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
    form = DatabaseForm()

    if request.method == 'POST':
        form = DatabaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('database-form')

    context = {'form':form,'databases':databases}
    return render(request, 'base/database_form.html', context)