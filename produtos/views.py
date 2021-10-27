import uuid
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from rest_framework.views import APIView
from produtos import services
from rest_framework.serializers import Serializer
import produtos
from produtos.serializers import ProdutoSerializer
from .services import ProdutoService
from django.contrib import messages

_SERVICE = ProdutoService()

def home(request):
    return render(request, 'home.html')


def home_produtos(request, produto_id=None):
    if produto_id is not None:
        _SERVICE.deletar_por_id(produto_id)
    elif request.method == "POST" and produto_id is None:
        serializer = ProdutoSerializer(data=request.POST)
        if not serializer.is_valid():
            messages.error(request, serializer.errors)
        else:
            serializer.save()
    produtos = _SERVICE.buscar_todos_produtos()
    paginator = Paginator(produtos, 3)
    page = request.GET.get('p')
    produtos = paginator.get_page(page)
    return render(request=request, template_name='home_produtos.html', context={'produtos': produtos})
    

def home_entrada_saida(request):
    return render(request, 'home_entrada_saida.html')

def home_editar_produto(request, produto_id:uuid):
    produtos = _SERVICE.buscar_produto_por_id(produto_id)

    if request.method == "GET":
        return render(request=request, template_name='home_editar_produto.html', context={'produtos': produtos})
    
    message = _SERVICE.editar_produto(produtos, request.POST)
    if message is not None:
        messages.info(request, "INFO")
        return render(request, template_name='home_editar_produto.html', context={"produtos":produtos})
    messages.success(request, "Salvo com sucesso")
    return render(request, 'home_editar_produto.html', context={"produtos":produtos})


    
