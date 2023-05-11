from django import forms


class ClienteForm(forms.Form):
    nome = forms.CharField(label="Nome: ", max_length=100, 
                           widget= forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'nome'}))
    
    
    email = forms.CharField(label="Email: ", max_length=100,
                            widget= forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'email'}))
    
    senha = forms.CharField(label="Senha: ", max_length=100, widget= forms.TextInput(attrs={'type': 'password'}))
    data_Nasc = forms.DateField(label='Data',widget=forms.DateInput(attrs={'type': 'date'}),
                                input_formats=['%d/%m/%y', '%Y-%m-%d' ])
    

class EnderecoForm(forms.Form):    
    
    cidade = forms.CharField(label="Cidade: ", max_length=30,
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}))
    
    bairro = forms.CharField(label="Bairro: ", max_length=30,
                             widget=forms.TextInput())
    
    rua   = forms.CharField(label="Rua: ", max_length=20,
                            widget=forms.TextInput())
    
    numero = forms.IntegerField(label="Numero: ",
                                widget=forms.TextInput())
    
    
    