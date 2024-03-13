from django.urls import path
from . import views

app_name = 'plataforma'

urlpatterns = [
    path('', views.home, name='home'),
    
    path('cadastro/', views.cadastro, name='cadastro'),

    path('alterar_senha/', views.alterar_senha, name='alterar_senha')
    
]
