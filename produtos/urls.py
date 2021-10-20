from django.urls import path, include
from .views import home, home_entrada_saida, home_produtos


urlpatterns = [
    path('', home, name="home"),
    path('produtos/', home_produtos, name="produtos"),
    path('entrada-saida/', home_entrada_saida, name="entrada-saida"),
]
