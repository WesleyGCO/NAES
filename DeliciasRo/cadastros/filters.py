from django_filters import FilterSet, CharFilter
from .models import CategoriaProduto, Produto, Pedido, Cliente

class CategoriaProdutoFilter(FilterSet):
    class Meta:
        model = CategoriaProduto
        fields = {
            'nome' : ['icontains'],
        }
        
class ProdutoFilter(FilterSet):
    class Meta:
        model = Produto
        fields = {
            'nome' : ['icontains'],
            'categoria' : ['exact'],
            'preco': ['gt', 'lt'],
        }
        
class PedidoFilter(FilterSet):
    cliente_nome = CharFilter(
        field_name='cliente__nome', 
        lookup_expr='icontains', 
        label='Nome do Cliente'
    )
    
    class Meta:
        model = Pedido
        fields = {
            'data_pedido': ['gte'],
            'status': ['exact'],
            'data_entrega': ['lte'],
        }
        
class ClienteFilter(FilterSet):
    class Meta:
        model = Cliente
        fields = {
            'nome' : ['icontains'],
            'telefone' : ['exact'],
        }