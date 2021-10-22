from django.urls import path, include
from .views import home, home_editar_produto, home_editar_salvar, home_entrada_saida, home_produtos


urlpatterns = [
    path('', home, name="home"),
    path('produtos/', home_produtos, name="produtos"),
    path('produtos/<uuid:produto_id>/', home_produtos, name="deletar_produtos"),
    path('editar/<uuid:produto_id>/', home_editar_produto, name="editar"),
    path('editar/salvar/', home_editar_salvar, name="editar_salvar"),
    path('entrada-saida/', home_entrada_saida, name="entrada-saida"),
]
