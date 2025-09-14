from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        # define qual campo vc quer escolher
        fields = ['nome', 'preco', 'estoque', 'categoria']