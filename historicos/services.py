import uuid

import produtos
from produtos.models import ProdutoModel
from .models import HistoricoModel

class ProdutoService():

    def buscar_todos_historicos(self) -> list[HistoricoModel]:
        return HistoricoModel.objects.all()

    def buscar_historico_por_id(self, id:id) -> HistoricoModel:
        return HistoricoModel.objects.filter(id=id).first()

    def buscar_historico_por_codigo(self, codigo:str) -> HistoricoModel:
        return HistoricoModel.objects.filter(codigo=codigo).first()