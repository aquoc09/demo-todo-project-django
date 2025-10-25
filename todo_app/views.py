from django.shortcuts import render, redirect
from .models import Task

def home(request):
    tasks = Task.objects.all()
    return render(request, 'home.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
    return redirect('home')

def toggle_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('home')

def delete_task(request, task_id):
    Task.objects.get(id=task_id).delete()
    return redirect('home')

