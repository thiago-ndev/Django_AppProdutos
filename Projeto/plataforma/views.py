from django.shortcuts import render, HttpResponse
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib.auth.models import User

from . models import models

# Create your views here.

HOME_PAGE = 'plataforma/index.html'
CADASTRO_PAGE = 'plataforma/cadastro.html'
LOGIN_PAGE = 'plataforma/login.html'


def home(request):
    return render(request, HOME_PAGE)

def login(request):
    try:
        if request.method == "POST":
            pass 
        
        
        # apenas parar de dar error, tira esse return depois
        return render(request, LOGIN_PAGE)
        
    except Exception as ex:
        msg = ex.args
        return render(request, LOGIN_PAGE, messages.add_message(request, constants.ERROR, f'{msg}'))
          

def cadastro(request):
    try:
         if request.method == "POST":
             return render(request, HOME_PAGE)
         
         
         
         else:
             username = request.POST.get('username')
             email = request.POST.get('email')
             senha = request.POST.get('senha')
             
             user = User.objects.get(username=username)
             
             if user:
                 return render(request, CADASTRO_PAGE, messages.add_message(request, constants.ERROR, 'usuario ja cadastrado'))
             
        
        
    except Exception as ex:
        msg = ex.args 
        return render(request, CADASTRO_PAGE)
    
