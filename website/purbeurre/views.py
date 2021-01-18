from django.shortcuts import redirect, render


def index(request):
    return render(request, 'home.html')


def myfood(request):
    return render(request, 'myfood.html')
