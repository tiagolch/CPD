from django.urls import path
from .views import *

urlpatterns = [
    # path('', index, name='index'),
    path('cadastro_tonners/', cadastro_tonners, name='cadastro_tonners'),
    path('atualizacao_tonners/<int:id>/', atualizacao_tonners, name='atualizacao_tonners'),
    path('delete_tonners/<int:id>/', delete_tonners, name='delete_tonners'),
    path('', listagem_tonners, name='listagem_tonners'),
]