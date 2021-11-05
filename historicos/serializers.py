from django.db.models import fields
from .models import HistoricoModel
from rest_framework import serializers
from produtos.services import ProdutoService

_SERVICE_PRODUTO = ProdutoService()

class HistoricoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricoModel
        fields = ('id', 'produto_id', 'funcionario', 'tipo',)

    def create(self, validated_data):
        produto = _SERVICE_PRODUTO.buscar_produto_por_codigo(validated_data.get('codigo_produto'))
        validated_data['produto_id'] = produto.id
        return super().create(validated_data)