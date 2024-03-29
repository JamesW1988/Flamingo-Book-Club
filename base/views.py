from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from .models import BookDatabase
from .forms import DatabaseForm
from django.http import JsonResponse, HttpRequest, HttpResponseRedirect


about = [
    {'id': 1, 'name': 'How this got started'},
    {'id': 2, 'name': 'Who is this program for'},
    {'id': 3, 'name': 'Why it is important'},
]


def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
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


def logoutUser(request):
    logout(request)
    return redirect('home')


def userProfile(request, pk):
    user = User.objects.get(id=pk)
    context = {'user': user}
    return render(request, 'base/profile.html', context)


def home(request):
    return render(request, 'base/home.html')


@login_required(login_url='login')
def database(request):
    databases = BookDatabase.objects.all()
    data = []

    for obj in databases:
        entry = {
            'title': obj.title,
            'author': obj.author,
            'description': obj.description,
            'grade_level': obj.grade_level,
            'inventory': obj.inventory,
        }
        data.append(entry)

    context = {'data': data}
    return JsonResponse(context)


def aboutpage(request):
    aboutpage = None
    context = {'aboutpage': aboutpage}
    return render(request, 'base/about.html', context)


@login_required(login_url='login')
def databaseForm(request):
    page = 'database_form'
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    databases = BookDatabase.objects.filter(
        Q(title__icontains=q) |
        Q(author__icontains=q) |
        Q(grade_level__icontains=q) |
        Q(inventory__icontains=q)
    )

    row_count = databases.count()
    form = DatabaseForm()

    if request.method == 'POST':
        form = DatabaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('database-form')

    context = {'form': form, 'databases': databases,
               'row_count': row_count, 'page': page}
    return render(request, 'base/database_form.html', context)
