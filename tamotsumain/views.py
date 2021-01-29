from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    return HttpResponse('This is Page')


def product(request):
    return render(request, 'home.html', {'greeting': 'Hello!'})
