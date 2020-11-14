from django.urls import path
from .views import *

urlpatterns = [
    # path('', index, name='index'),
    path('cadastro_tonners/', cadastro_tonners, name='cadastro_tonners'),
    path('abertura_chamado/', abertura_chamado, name='abertura_chamado'),
    path('atualizacao_tonners/<int:id>/', atualizacao_tonners, name='atualizacao_tonners'),
    path('atualizacao_chamado/<int:id>/', atualizacao_chamado, name='atualizacao_chamado'),
    path('delete_tonners/<int:id>/', delete_tonners, name='delete_tonners'),
    path('delete_chamado/<int:id>/', delete_chamado, name='delete_chamado'),
    path('listagem_tonners', listagem_tonners, name='listagem_tonners'),
    path('listagem_chamado', listagem_chamado, name='listagem_chamado'),
]