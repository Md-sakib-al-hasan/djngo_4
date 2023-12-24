from django.shortcuts import render, redirect
from .import forms
from .import models
from category.models import Category
# Create your views here.
def add_tasks(request):
    
    if request.method == 'POST':
        task_form = forms.TaskFrom(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('show_task')

    else:
        task_form = forms.TaskFrom()
    return render(request,'add_task.html',{'form':task_form})

def edit_tasks(request,id):
    tasks = models.Task.objects.get(pk=id)
    models.Task.objects.filter(is_completed = False)== True

    task_form = forms.TaskFrom(instance=tasks)
    if request.method == 'POST':
        task_form = forms.TaskFrom(request.POST, instance=tasks)
        if task_form.is_valid():
            task_form.save()
            return redirect('show_task')

    return render(request,'add_task.html',{'form':task_form})

def delete_tasks(request,id):
    tasks = models.Task.objects.get(pk=id)
    tasks.delete()
    return redirect('show_task')