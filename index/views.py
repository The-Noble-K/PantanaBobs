from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})

def menu(request):
    return render(request, 'menu.html', {})

def events(request):
    return render(request, 'events.html', {})

