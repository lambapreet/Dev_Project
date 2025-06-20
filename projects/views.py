from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import ProjectForm

# Create your views here.

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects/project.html', {'projects': projects})


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    return render(request, 'projects/single-project.html', {'project': projectObj})


@login_required(login_url='login')
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect('account')
    context = {'form': form}
    return render(request, 'projects/project_form.html', context)


@login_required(login_url='login')
def updateProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project')
    context = {'form': form}
    return render(request, 'projects/project_form.html', context)


@login_required(login_url='login')
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('project')
    context = {'object': project}
    return render(request, 'delete.html', context)





















'''
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import ProjectForm

# Create your views here.

def project(request):
    projects = ProjectModel.objects.all()
    return render(request, 'projects/project.html',{'projects':projects})


def projectView(request, pk):
    projectObj = ProjectModel.objects.get(id=pk)
    return render(request, 'projects/index.html', {'project':projectObj})


@login_required(login_url='login')
def createView(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('project')
    context = {'form':form}
    return render(request, 'projects/project_form.html', context)


@login_required(login_url='login')
def UpdateView(request,pk):
    project = ProjectModel.objects.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES,instance=project )
        if form.is_valid():
            form.save()
            return redirect('project')
    context = {'form':form}
    return render(request, 'projects/project_form.html', context)


@login_required(login_url='login')
def deleteView(request,pk):
    project = ProjectModel.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('project')
    context = {'object':project}
    return render(request, 'projects/delete.html', context)


'''