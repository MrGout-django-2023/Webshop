from django.shortcuts import render

def index(request):
    return render(request, 'news/index.html', context={
        'title': 'Новини',
        'page': 'index',
        'app': 'news',
    })


