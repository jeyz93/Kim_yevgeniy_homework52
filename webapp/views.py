from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from webapp.models import Tasks


def index_view(request: WSGIRequest):
    tasks = Tasks.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'index.html', context)


def task_detail(request):
    id = request.GET.get('id')
    tasks = Tasks.objects.get(id=id)
    return render(request, 'task.html',context={'tasks':tasks})


def create_task_view(request):
    if request.method == "GET":
        return render(request, 'task_add.html')
    return render(request, 'index.html')
