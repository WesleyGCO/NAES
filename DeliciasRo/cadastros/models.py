from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Categoria de produto, como "Docinho", "Salgado", "Bebida", "Bolo", "Festa na Caixa"
class CategoriaProduto(models.Model):
    nome = models.CharField(max_length=50, verbose_name='Categoria')

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    telefone = models.CharField(max_length=20, verbose_name='Telefone')
    endereco = models.CharField(max_length=200, null=True, verbose_name='Endereço', blank=True)
    data_cadastro = models.DateTimeField(auto_now_add=True, verbose_name='Data de Cadastro')

    def __str__(self):
        return "{} - ({}) - {}".format(self.nome, self.telefone, self.endereco)


# Produto base
class Produto(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    categoria = models.ForeignKey(CategoriaProduto, on_delete=models.SET_NULL, null=True, verbose_name='Categoria')
    data_cadastro = models.DateTimeField(auto_now_add=True, verbose_name='Data de Cadastro')
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço', null=True)
    criado_por = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Criado por')

    def __str__(self):
        return "{}".format(self.nome)

# Pedido que contém vários produtos ou conjuntos
class Pedido(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome', blank=True, null=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    data_pedido = models.DateTimeField(auto_now_add=True, verbose_name='Data do Pedido')
    data_entrega = models.DateTimeField(null=True, verbose_name='Data de Entrega')
    valor_adiantado = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Valor Adiantado')
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Valor Total')
    status = models.CharField(max_length=50, default="Pendente", verbose_name="Status", choices=[("Pendente", "Pendente"), ("Entregue", "Entregue"), ("Cancelado", "Cancelado")])
    criado_por = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Criado por')
    
    def __str__(self):
        return "{} - {}".format(self.cliente, self.data_pedido)

# Produtos individuais adicionados a um pedido, com a quantidade
class ProdutoPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='pedido', verbose_name='Pedido')
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    quantidade = models.IntegerField(verbose_name='Quantidade')
    descricao_personalizada = models.TextField(null=True, blank=True, verbose_name='Descrição Personalizada')
    data_cadastro = models.DateTimeField(auto_now_add=True, verbose_name='Data de Cadastro')

    def __str__(self):
        return "{} - {} unidades".format(self.produto.nome, self.quantidade)