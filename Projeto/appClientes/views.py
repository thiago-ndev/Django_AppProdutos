from django.shortcuts import render
from django.http import HttpResponse 
from django.template import loader
from django.contrib import messages
from django.contrib.messages import constants
from .forms import ClienteForm, EnderecoForm
from .models import Cliente, Endereco

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
    
    return render(request, CADASTRO_PAGE, {'form_cliente': form_cliente, 'form_endereco': form_endereco} )

def cadastrar(request):
    try:
        form_cliente = ClienteForm(request.POST)
        form_endereco = EnderecoForm(request.POST)
        if request.method == "POST":
            cliente = Cliente()
            endereco = Endereco()
            if form_cliente.is_valid() and form_endereco.is_valid():
                cliente.nome = form_cliente.cleaned_data['nome']
                cliente.email = form_cliente.cleaned_data['email']
                cliente.senha = form_cliente.cleaned_data['senha']
                cliente.data_Nasc =form_cliente.cleaned_data['data_Nasc']
                endereco.cidade = form_endereco.cleaned_data['cidade']
                endereco.bairro = form_endereco.cleaned_data['bairro']
                endereco.rua = form_endereco.cleaned_data['rua']
                endereco.numero = form_endereco.cleaned_data['numero']
                
                cliente.save()
                endereco.save()
                    

            else:
                msg = form_cliente.errors
                msg1 = form_endereco.errors
                print(msg)
                print(msg1)
            
        else:
            raise Exception(messages.add_message(request, constants.ERROR, "MethodEnvioError, Use POST para enviar formulários."))
        
        return print('aqui')                    
        
    except Exception as ex:
        msg = ex.args
        return render(request, CADASTRO_PAGE,messages.add_message(request, constants.ERROR, msg))
    
def buscar(request):
    pass

def lista(request):
    pass  

def alterar(request):
    pass

def excluir(request):
    pass

