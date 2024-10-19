from django.urls import path
from .views import CategoriaProdutoCreate, PedidoCreate, ProdutoCreate, ClienteCreate
from .views import CategoriaProdutoUpdate, PedidoUpdate, ProdutoUpdate, ClienteUpdate
from .views import CategoriaProdutoDelete, PedidoDelete, ProdutoDelete, ClienteDelete
from .views import CategoriaProdutoList, PedidoList, ProdutoList, ClienteList

urlpatterns = [
    path('cadastrar/categoria/', CategoriaProdutoCreate.as_view(), name='cadastrar-categoria'),
    path('atualizar/categoria/<int:pk>/', CategoriaProdutoUpdate.as_view(), name='atualizar-categoria'),
    path('excluir/categoria/<int:pk>/', CategoriaProdutoDelete.as_view(), name='excluir-categoria'),
    path('listar/categorias/', CategoriaProdutoList.as_view(), name='listar-categoria'),
    
    path('cadastrar/pedido/', PedidoCreate.as_view(), name='cadastrar-pedido'),
    path('atualizar/pedido/<int:pk>/', PedidoUpdate.as_view(), name='atualizar-pedido'),
    path('excluir/pedido/<int:pk>/', PedidoDelete.as_view(), name='excluir-pedido'),
    path('listar/pedidos/', PedidoList.as_view(), name='listar-pedido'),
    
    path('cadastrar/produto/', ProdutoCreate.as_view(), name='cadastrar-produto'),
    path('atualizar/produto/<int:pk>/', ProdutoUpdate.as_view(), name='atualizar-produto'),
    path('excluir/produto/<int:pk>/', ProdutoDelete.as_view(), name='excluir-produto'),
    path('listar/produtos/', ProdutoList.as_view(), name='listar-produto'),
    
    path('cadastrar/cliente/', ClienteCreate.as_view(), name='cadastrar-cliente'),
    path('atualizar/cliente/<int:pk>/', ClienteUpdate.as_view(), name='atualizar-cliente'),
    path('excluir/cliente/<int:pk>/', ClienteDelete.as_view(), name='excluir-cliente'),
    path('listar/clientes/', ClienteList.as_view(), name='listar-cliente'),
]
