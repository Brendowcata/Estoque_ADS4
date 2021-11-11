import uuid

import produtos
from produtos.models import ProdutoModel
from produtos.services import ProdutoService
from .models import HistoricoModel

_SERVICE_PRODUTO = ProdutoService()

class HistoricoService():

    def salvar_historico(self, data:dict):
        produto = _SERVICE_PRODUTO.buscar_produto_por_id(data.get("produto_id"))
        historico = HistoricoModel(
            produto_id=produto,
            funcionario=data.get("funcionario"),
            tipo=data.get("tipo"),
            descricao=data.get("descricao"),
            quantidade=data.get("quantidade"),
        )
        historico.save()

    def buscar_todos_historicos(self) -> list[HistoricoModel]:
        return HistoricoModel.objects.all()

    def buscar_historico_por_id(self, id:id) -> HistoricoModel:
        return HistoricoModel.objects.filter(id=id).first()

    def buscar_historico_por_codigo(self, codigo:str) -> HistoricoModel:
        return HistoricoModel.objects.filter(codigo=codigo).first()