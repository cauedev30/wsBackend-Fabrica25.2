from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto
from .forms import ProdutoForm
import requests # biblioteca que 'chama' a API

# view para a página inicial (listar Produtos)
def lista_produtos(request):
    # lógica pra pegar a API de conversão ---- 
    cotacao_dolar = 'N/A'
    try:
        # API gratuita/publica de cotação de moedas
        response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
        data = response.json()
        # pega a cotação para o Real (BRL)
        cotacao_dolar = data['rates']['BRL']
    except requests.RequestException:
        # caso a API falhe, não mata o site
        cotacao_dolar = 'Erro ao buscar cotação'
    #  Fim da API ---- 


    produtos = Produto.objects.all().order_by('nome') # procura todos os produtos no banco
    context = {
        'produtos': produtos,
        'cotacao_dolar': cotacao_dolar
    }
    return render(request, 'padaria_app/lista_produtos.html', context)
    

# view pra add Produto
def adicionar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'padaria_app/form_produto.html', {'form': form, 'acao': 'Adicionar'})


# view para editar Produto
def editar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'padaria_app/form_produto.html', {'form': form, 'acao': 'Editar'})


# view para deletar Produto
def deletar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == 'POST':
        produto.delete()
        return redirect('lista_produtos')
    return render(request, 'padaria_app/confirmar_delete.html', {'produto': produto})

# Create your views here.
