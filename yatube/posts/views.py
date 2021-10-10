from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('Главная страница')

def group_posts(request, slug):
    return HttpResponse(f'Тут есть фильтр {slug}')