from django.shortcuts import render, HttpResponse
from django.contrib.messages import constants
from django.contrib import messages


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
    return render(request, CADASTRO_PAGE)
    
