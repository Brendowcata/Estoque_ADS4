from django.http import request
from django.shortcuts import render
from historicos.serializers import HistoricoSerializer

from historicos.services import HistoricoService
from django.core.paginator import Paginator
from django.contrib import messages
from produtos.models import ProdutoModel

from produtos.services import ProdutoService

_SERVICE = HistoricoService()

def historico(request):
    if request.method == "POST":
        serializer = HistoricoSerializer(data=request.POST)
        if not serializer.is_valid():
            messages.error(request, serializer.errors)
        else:
            serializer.save()
    produtos = ProdutoService.buscar_todos_produtos(ProdutoModel)
    historicos = _SERVICE.buscar_todos_historicos()
    paginator = Paginator(historicos, 3)
    page = request.GET.get('p')
    historicos = paginator.get_page(page)
    return render(request=request, template_name='historico.html', context={'historicos': historicos, 'produtos': produtos})


