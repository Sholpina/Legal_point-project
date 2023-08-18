from django.shortcuts import render
from .models import Project, About
from datetime import datetime


def home(request):
        projects = Project.objects.all()
        data_footer = datetime.now().strftime('%b %d %Y')
        return render(request, 'portfolio/home.html', {'projects': projects, 'data_footer': data_footer})


def signupuser(request):
        return render(request, 'portfolio/signupuser.html')


def aboutme(request):
        about = About.objects.all()
        return render(request, 'portfolio/aboutme.html', {'about': about})
