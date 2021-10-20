from django.shortcuts import render
from django.core.paginator import Paginator
from rest_framework.views import APIView
from produtos import services
from .services import ProdutoService

_SERVICE = ProdutoService()

def home(request):
    return render(request, 'home.html')


def home_produtos(request):
    produtos = _SERVICE.buscar_todos_produtos()
    paginator = Paginator(produtos, 3)
    page = request.GET.get('p')
    produtos = paginator.get_page(page)
    return render(request=request, template_name='home_produtos.html', context={'produtos': produtos})


def home_entrada_saida(request):
    return render(request, 'home_entrada_saida.html')
    