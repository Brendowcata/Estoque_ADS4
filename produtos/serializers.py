from django.db.models import fields
from .models import ProdutoModel
from rest_framework import serializers

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProdutoModel
        fields = ('id','nome', 'codigo')