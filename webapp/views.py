from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from webapp.models import Tasks


# def index_view(request: WSGIRequest):
#     # articles = Article.objects.all()
#     # context = {
#     #     'articles' : articles
#     # }
#     return render(request, 'index.html')
#


def index_view(request: WSGIRequest):
    tasks = Tasks.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'index.html', context)
