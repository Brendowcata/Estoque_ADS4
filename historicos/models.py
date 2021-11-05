from django.db import models
import uuid
from django_extensions.db.models import TimeStampedModel

from produtos.models import ProdutoModel

class HistoricoModel(TimeStampedModel):
     id = models.UUIDField(
        db_column="ID",
        primary_key= True,
        editable= False,
        unique= True,
        default= uuid.uuid4
    )

     produto_id = models.ForeignKey(
        ProdutoModel, 
        on_delete=models.CASCADE
    )

     data_entrada = models.DateField()

     funcionario = models.CharField(max_length=50)

     tipo = models.CharField(max_length=7)

     descricao = models.TextField(default=None)

     def __str__(self) -> str:
         return f"{self.id}"
     
     class Meta:
         db_table = 'HISTORICO'
         verbose_name = 'Historico'
         verbose_name_plural = 'Historicos'
