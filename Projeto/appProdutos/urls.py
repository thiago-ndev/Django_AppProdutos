from django.urls import path
from .import views


app_name = 'appProdutos'

urlpatterns = [

    path('', views.home, name='home'),

    path('Cadastro/', views.cadastro, name='cadastro'),

    path('Cadastrar/', views.cadastrar, name='cadastrar'),

    path('Busca/', views.busca, name='busca'),

    path('Lista/', views.lista, name='lista'),

    path('Alterar/<int:codigo>/', views.alterar, name='alterar'),

    path('Excluir/<int:codigo>/', views.excluir, name='excluir'),

    path('Busca/enviar_post/', views.pesquisar, name="pesquisar"),
]