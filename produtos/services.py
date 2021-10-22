import uuid

import produtos
from .models import ProdutoModel

class ProdutoService():

    def buscar_todos_produtos(self) -> list[ProdutoModel]:
        return ProdutoModel.objects.all()

    def buscar_produto_por_id(self, id:uuid) -> ProdutoModel or None:
        return ProdutoModel.objects.filter(id=id).first()

    def deletar_por_id(self, id:uuid) -> None:
        return ProdutoModel.objects.filter(id=id).delete()

    def editar_contato(produto:produtos, post:dict) -> None:
        produto.nome = post['nome']
        produto.codigo = post['codigo']
        produto.save()
