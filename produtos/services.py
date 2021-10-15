import uuid
from .models import ProdutoModel

class ProdutoService():

    def buscar_todos_produtos(self) -> list(ProdutoModel):
        return ProdutoModel.objects.all()

    def buscar_produto_por_id(self, id:uuid) -> ProdutoModel or None:
        return ProdutoModel.objects.filter(id=id).first()
