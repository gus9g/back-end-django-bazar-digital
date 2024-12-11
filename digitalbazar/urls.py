from django.urls import path
from .views import (adicionar_produto,
    listar_todos_produtos,
    listar_produto_por_nome,
    alterar_produto,
    excluir_produto,
    incluir_por_planilha,
    incluir_por_txt,)

urlpatterns = [
    path('adicionar', adicionar_produto, name='adicionar_produto'),
    path('listar', listar_todos_produtos, name='listar_todos_produtos'),
    path('listar/<str:nome>', listar_produto_por_nome, name='listar_produto_por_nome'),
    path('alterar/<int:id>', alterar_produto, name='alterar_produto'),
    path('excluir/<int:id>', excluir_produto, name='excluir_produto'),
    path('incluir/csv', incluir_por_planilha, name='incluir_por_planilha'),
    path('incluir/txt', incluir_por_txt, name='incluir_por_txt'),
]