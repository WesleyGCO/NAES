# Generated by Django 4.2.16 on 2024-10-19 21:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaProduto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('telefone', models.CharField(max_length=20, verbose_name='Telefone')),
                ('endereco', models.CharField(blank=True, max_length=200, null=True, verbose_name='Endereço')),
                ('data_cadastro', models.DateTimeField(auto_now_add=True, verbose_name='Data de Cadastro')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nome')),
                ('data_pedido', models.DateTimeField(auto_now_add=True, verbose_name='Data do Pedido')),
                ('data_entrega', models.DateTimeField(null=True, verbose_name='Data de Entrega')),
                ('valor_adiantado', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Valor Adiantado')),
                ('valor_total', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Valor Total')),
                ('status', models.CharField(choices=[('Pendente', 'Pendente'), ('Entregue', 'Entregue'), ('Cancelado', 'Cancelado')], default='Pendente', max_length=50, verbose_name='Status')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.cliente')),
                ('criado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Criado por')),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('data_cadastro', models.DateTimeField(auto_now_add=True, verbose_name='Data de Cadastro')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10, null=True, verbose_name='Preço')),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cadastros.categoriaproduto', verbose_name='Categoria')),
                ('criado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Criado por')),
            ],
        ),
        migrations.CreateModel(
            name='ProdutoPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(verbose_name='Quantidade')),
                ('descricao_personalizada', models.TextField(blank=True, null=True, verbose_name='Descrição Personalizada')),
                ('data_cadastro', models.DateTimeField(auto_now_add=True, verbose_name='Data de Cadastro')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pedido', to='cadastros.pedido', verbose_name='Pedido')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.produto')),
            ],
        ),
    ]