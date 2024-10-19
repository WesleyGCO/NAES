from django.contrib import admin
# Importar modelos
from .models import CategoriaProduto, Cliente, Produto, ProdutoPedido, Pedido

# Register your models here.
admin.site.register(CategoriaProduto)
admin.site.register(Cliente)
admin.site.register(Produto)    
admin.site.register(ProdutoPedido)
admin.site.register(Pedido)