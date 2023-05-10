from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .forms import CadastroForm
from django.contrib import messages
from django.contrib.messages import constants
from .models import Produto
import json
# Create your views here.

# macetinho do Sérgio muito robado
CADASTRO_PAGE = 'appProdutos/cadastro.html'
BUSCA_PAGE = 'appProdutos/busca.html'
LISTA_PAGE = 'appProdutos/lista.html'



def home(request):
    template = loader.get_template('appProdutos/index.html')
    return HttpResponse(template.render())

def cadastro(request):
    form = CadastroForm()
    return render(request,CADASTRO_PAGE, {'form': form})

def cadastrar(request):

    try:
        if request.method == 'POST':
            form = CadastroForm(request.POST)
            if form.is_valid():
                produto = Produto()
                produto.nome = form.cleaned_data['nome']
                produto.preco = form.cleaned_data['preco']
                produto.quantidade = form.cleaned_data['quantidade']

                codigo = form.cleaned_data['codigo']
            

                if codigo:
                    produto.codigo = codigo
                    messages.add_message(request, constants.WARNING, "Produto Alterado.")

                produto.save()
                
            else:
                msg = form.errors
                return render(request,CADASTRO_PAGE,{'form':CadastroForm, 'msg':msg})
            
            messages.add_message(request, constants.SUCCESS, "Produto Cadastrado.")
            return render(request,CADASTRO_PAGE,{'form':CadastroForm,'msg':msg})
        
        else:
            raise Exception('MethodEnvioError, Use POST para Formularios.')
        
    except Exception as ex:
        msg = ex.args
        return render(request,CADASTRO_PAGE,{'form':CadastroForm,'msg':msg})

def busca(request):
    return render(request, BUSCA_PAGE)

def lista(request):
    produtos = Produto.objects.order_by('codigo').all()
    return render(request, LISTA_PAGE, {'produtos': produtos})

def alterar(request,codigo):

    try:
        produto = Produto.objects.get(pk=codigo)
        form = CadastroForm(initial={
            'nome': produto.nome,
            'preco': produto.preco,
            'quantidade': produto.quantidade,
            'codigo': produto.codigo

        })
        
        return render(request,CADASTRO_PAGE,{'form':form})

    except Exception as ex:
        msg = ex.args
        render(request, LISTA_PAGE, {'produtos': Produto.objects.all(), 'msg': msg })

def excluir(request,codigo):
    produtos = Produto.objects.all()
    try:
        produto = Produto.objects.get(pk = codigo)
        result = produto.delete()

        if result[0] > 0:
            messages.add_message(request, constants.ERROR, "Produto deletado.")
            
        else:
            messages.add_message(request, constants.ERROR, "Produto não encontrado.")
            
            
        return render(request,LISTA_PAGE,{'produtos':produtos})

    except Exception as ex:
        msg = ex.args
        render(request, LISTA_PAGE, {'produtos':produtos, 'msg': msg})

def pesquisar(request):

    try:
        if request.method == 'POST':
            nome = request.POST['nome']
            # efetuar uma busca no banco de dados
            # LIKE %nome% -> contenha a palavra 'copo'
            produtos = Produto.objects.filter(nome__icontains =nome)
            response = {}

            for indice, produto in enumerate(produtos):
                p = {}
                p['codigo'] = produto.codigo
                p['nome'] = produto.nome
                p['preco'] = produto.preco
                p['quantidade'] = produto.quantidade
                response[indice] = p

            response['t'] = len(produtos)

            return HttpResponse(json.dumps(response),
                                content_type='application/json')


        else:
            raise Exception('MethodEnvioError, use POST para formulários')

    except Exception as ex:
        msg = ex.args
        return HttpResponse(json.dumps({"msg": msg}),
                            content_type='application/json')