from django.shortcuts import render, redirect
from .models import Project,Review,Tag
from django.http import HttpResponse
from .forms import ProjectForm

# Create your views here.

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {'projects': projects})


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    return render(request, 'projects/single-project.html', {'project': projectObj})


def createProject(request):
    pass


def updateProject(request, pk):
    pass

def deleteProject(request,pk):
    pass