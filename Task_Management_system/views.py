from django.shortcuts import render
from task.models import Task
from category.models import Category
# Create your views here.
def Management (request):
    return render(request,'management.html')

def show_task(request):
    data = Task.objects.all()
    return render(request,'show_task.html',{"data":data})
