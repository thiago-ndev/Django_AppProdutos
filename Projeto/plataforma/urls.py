from django.urls import path
from . import views

app_name = 'plataforma'

urlpatterns = [
    path('', views.home, name='home'),
    
    path('login/', views.login, name='login'),
    
    path('cadastro/', views.cadastro, name='cadastro')
    
]
