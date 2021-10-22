from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.core.paginator import Paginator
from rest_framework.views import APIView
from produtos import services
import produtos
from produtos.serializers import ProdutoSerializer
from .services import ProdutoService

_SERVICE = ProdutoService()

def home(request):
    return render(request, 'home.html')


def home_produtos(request, produto_id=None):
    if produto_id is not None:
        _SERVICE.deletar_por_id(produto_id)
    
    produtos = _SERVICE.buscar_todos_produtos()
    paginator = Paginator(produtos, 3)
    page = request.GET.get('p')
    produtos = paginator.get_page(page)
    return render(request=request, template_name='home_produtos.html', context={'produtos': produtos})
    

def home_entrada_saida(request):
    return render(request, 'home_entrada_saida.html')

def home_editar_produto(request, produto_id=None):
    produtos = _SERVICE.buscar_produto_por_id(produto_id)
    return render(request=request, template_name='home_editar_produto.html', context={'produtos': produtos})

def home_editar_salvar(request, produto_id=None):
    produtos = _SERVICE.buscar_produto_por_id(produto_id)    
    _SERVICE.editar_contato(produtos, request.POST)
    return HttpResponseRedirect('/')
    