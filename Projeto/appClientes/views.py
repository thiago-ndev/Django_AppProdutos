from django.shortcuts import render
from django.http import HttpResponse 
from django.template import loader
from .forms import ClienteForm, EnderecoForm

CADASTRO_PAGE = 'appClientes/cadastro.html'
BUSCA_PAGE = 'appClientes/busca.html'
LISTA_PAGE = 'appClientes/lista.html'

# Create your views here.

def home(request):
    template = loader.get_template('appClientes/index.html')
    return HttpResponse(template.render())

def cadastro(request):        
    form_cliente = ClienteForm()
    form_endereco =  EnderecoForm()
    
    return render(request,CADASTRO_PAGE, {'form_cliente':form_cliente})

def alterar(request):
    pass

def buscar(request):
    pass

def excluir(request):
    pass

def lista(request):
    pass  
