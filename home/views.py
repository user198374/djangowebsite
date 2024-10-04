from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'home/index.html')

def auth_app(request):
    return render(request, 'auth_app/inscription.html')

def connexion(request):
    return render(request, 'auth_app/connexion.html')