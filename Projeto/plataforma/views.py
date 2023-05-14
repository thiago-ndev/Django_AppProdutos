from django.shortcuts import render, HttpResponse
from . models import models

# Create your views here.

HOME_PAGE = 'plataforma/index.html'
CADASTRO_PAGE = 'plataforma/cadastro.html'
LOGIN_PAGE = 'plataforma/login.html'


def home(request):
    return render(request, HOME_PAGE)

def login(request):
    return render(request, LOGIN_PAGE)
     

def cadastro(request):
    return render(request, CADASTRO_PAGE)
    
