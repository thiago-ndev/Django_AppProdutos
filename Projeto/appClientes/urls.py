from django.urls import path
from . import views

app_name = "appClientes"

urlpatterns = [
    path('', views.home, name="home"),
    
    path('cadastro/', views.cadastro, name="cadastro"),
    
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    
    path('buscar/', views.buscar, name="buscar"),
    
    path('lista/', views.lista, name="lista"),
    
    path('alterar/<int:codigo>/', views.alterar, name='alterar'),
    
    path('excluir/<int:codigo>/', views.excluir, name='excluir')
        
]

