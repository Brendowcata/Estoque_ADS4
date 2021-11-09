from django.urls import path, include
from .views import historico


urlpatterns = [
    path('historico/', historico, name="historico"),
]