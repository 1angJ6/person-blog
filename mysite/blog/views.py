from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


# HTTP Error 400
def error(request):
    return render(request, '404.html', status=404)
