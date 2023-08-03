from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .models import Project
from django.utils import timezone
from django.contrib.auth.decorators import login_required


def home(request):
        projects = Project.objects.all()
        data_footer = datetime.now().strftime("%B %d, %Y")
        return render(request, 'portfolio/home.html', {'projects': projects, 'data_footer': data_footer})


def dashboard(request):
        # projects = Project.objects.all()
        dashboard_data= datetime.now().strftime("%B %d, %Y")
        return render(request, 'portfolio/dashboard.html', {'dashboard': dashboard_data})


def about(request):
        # projects = Project.objects.all()
        about_data= datetime.now().strftime("%B %d, %Y")
        return render(request, 'portfolio/about-us.html', {'about': about_data})


def signupuser(request):
        if request.method == 'GET':
                return render(request, 'portfolio/signinuser.html', {'form': UserCreationForm()})
        else:
                # Получение данных из формы регистрации
                email = request.POST['exampleInputEmail1']
                password = request.POST['exampleInputPassword1']

        if request.POST['exampleInputPassword1'] == request.POST['exampleInputPassword2']:
                try:  # Создание нового пользователя
                        user = User.objects.create_user(email=email, password=password)
                        user.save()
                        login(request, user)
                        return redirect('userdashbord')
                except IntegrityError:
                        return render(request, 'todo/signinuser.html', {'form': UserCreationForm(),
                                                                        'error': 'That username has already been taken. Please choose a new username'})
        else:
                return render(request, 'portfolio/signinuser.html',
                              {'form': UserCreationForm(), 'error': 'Passwords did not match'})


#
def signinuser(request):
        if request.method == 'GET':
                return render(request, 'portfolio/signinuser.html', {'form': AuthenticationForm()})
        else:
                user = authenticate(request, email=request.POST['exampleInputPassword'],
                                    password=request.POST['exampleInputPassword1'])
                if user is None:
                        return render(request, 'portfolio/signup.html',
                                      {'form': AuthenticationForm(), 'error': 'Username and password did not match'})
                else:
                        login(request, user)
                        return redirect('userdashbord')


#
@login_required
def logoutuser(request):
        if request.method == 'POST':
                logout(request)
                return redirect('home')
#
# @login_required
# def createtodo(request):
#     if request.method == 'GET':
#         return render(request, 'todo/createtodo.html', {'form':TodoForm()})
#     else:
#         try:
#             form = TodoForm(request.POST)
#             newtodo = form.save(commit=False)
#             newtodo.user = request.user
#             newtodo.save()
#             return redirect('currenttodos')
#         except ValueError:
#             return render(request, 'todo/createtodo.html', {'form':TodoForm(), 'error':'Bad data passed in. Try again.'})
#
# @login_required
# def currenttodos(request):
#     todos = Todo.objects.filter(user=request.user, datecompleted__isnull=True)
#     return render(request, 'todo/currenttodos.html', {'todos':todos})
#
# @login_required
# def completedtodos(request):
#     todos = Todo.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
#     return render(request, 'todo/completedtodos.html', {'todos':todos})
#
# @login_required
# def viewtodo(request, todo_pk):
#     todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
#     if request.method == 'GET':
#         form = TodoForm(instance=todo)
#         return render(request, 'todo/viewtodo.html', {'todo':todo, 'form':form})
#     else:
#         try:
#             form = TodoForm(request.POST, instance=todo)
#             form.save()
#             return redirect('currenttodos')
#         except ValueError:
#             return render(request, 'todo/viewtodo.html', {'todo':todo, 'form':form, 'error':'Bad info'})
#
# @login_required
# def completetodo(request, todo_pk):
#     todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
#     if request.method == 'POST':
#         todo.datecompleted = timezone.now()
#         todo.save()
#         return redirect('currenttodos')
#
# @login_required
# def deletetodo(request, todo_pk):
#     todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
#     if request.method == 'POST':
#         todo.delete()
#         return redirect('currenttodos')
