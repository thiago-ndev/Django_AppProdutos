from django import forms

class CadastroForm(forms.Form):
    codigo = forms.IntegerField(required=False, widget= forms.HiddenInput())
    nome = forms.CharField(label='Produto : ',max_length=100, widget=forms.TextInput(
        attrs={'class' : 'form-control', 'placeholder': 'nome'}
    ))
    preco = forms.FloatField(label='Preço: ', widget=forms.TextInput(
        attrs={'class': 'form-control', 'type':'number'}
    ))
    quantidade = forms.IntegerField(label='Quantidade: ', widget=forms.TextInput(
        attrs={'class': 'form-control', 'type':'number'}

    ))
