from django.urls import path
from . import views

app_name = "appClientes"

urlpatterns = [
    path('', views.home, name="home"),
    
    path('cadastro/', views.cadastro, name="cadastro"),
    
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    
    path('busca/', views.busca, name="busca"),
    
    path('lista/', views.lista, name="lista"),
    
    path('alterar/<int:id>/', views.alterar, name='alterar'),
    
    path('excluir/<int:id>/', views.excluir, name='excluir')
        
]

