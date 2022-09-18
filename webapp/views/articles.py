# from django.shortcuts import render
#
#
# def add_view(request):
#     if request.method == 'GET':
#         return render(request, 'article-create.html')
#     context = {
#         'title': request.POST.get('title'),
#         'title': request.POST.get('author'),
#         'text': request.POST.get('text'),
#     }
#     return render(request, 'article.html', context=context)