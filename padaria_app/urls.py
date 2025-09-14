# aqui no urls é a definição do CRUD 
from django.urls import path
from . import views

urlpatterns = [
    # rota para a pagina inicial que lista os produtos
    path('', views.lista_produtos, name='lista_produtos'),
    # rota pra página add um novo produto
    path('produto/adicionar/', views.adicionar_produto, name='adicionar_produto'),
    # rota pra editar um produto existente
    path('produto/editar/<int:id>/', views.editar_produto, name='editar_produto'),
    # rota pra deletar um produto
    path('produto/deletar/<int:id>/', views.deletar_produto, name='deletar_produto'),
]