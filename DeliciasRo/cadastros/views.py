from datetime import datetime
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import CategoriaProduto, Cliente, Produto, ProdutoPedido, Pedido

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import get_object_or_404
from .forms import ProdutoPedidoFormSet, PedidoForm

from django_filters.views import FilterView
from .filters import CategoriaProdutoFilter, ProdutoFilter, PedidoFilter, ClienteFilter

from django.contrib.messages.views import SuccessMessageMixin

#region CategoriaProduto

class CategoriaProdutoCreate(LoginRequiredMixin, CreateView, SuccessMessageMixin):
    login_url = reverse_lazy('login')
    model = CategoriaProduto
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-categoria')
    success_message = 'Categoria %(nome)s cadastrada com sucesso!'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastrar Categoria'
        context['botao'] = 'Cadastrar'
        
        return context
    
class CategoriaProdutoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = CategoriaProduto
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-categoria')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Categoria'
        context['botao'] = 'Atualizar'
        
        return context
    
class CategoriaProdutoDelete(LoginRequiredMixin, DeleteView, SuccessMessageMixin):
    login_url = reverse_lazy('login')
    model = CategoriaProduto
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-categoria')
    success_message = 'Categoria excluída com sucesso!'
    
    # def get_object(self, queryset = None):
    #     #self.object = CategoriaProduto.objects.get(id=self.kwargs['pk'], criado_por=self.request.user)
    #     self.object = get_object_or_404(CategoriaProduto, id=self.kwargs['pk'], criado_por=self.request.user)
    #     return self.object
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Excluir Categoria'
        context['botao'] = 'Excluir'
        
        return context
    
    
class CategoriaProdutoList(LoginRequiredMixin, FilterView):
    login_url = reverse_lazy('login')
    model = CategoriaProduto
    template_name = 'cadastros/listas/categoria.html'
    context_object_name = 'categorias'
    filterset_class = CategoriaProdutoFilter
    
    # def get_queryset(self):
    #     self.object_list = CategoriaProduto.objects.filter()
    #     return self.object_list
    
#endregion CategoriaProduto

#region Pedido

class PedidoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Pedido
    form_class = PedidoForm  # Atualizado para usar o PedidoForm
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-pedido')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = ProdutoPedidoFormSet(self.request.POST)
        else:
            context['formset'] = ProdutoPedidoFormSet()
        context['titulo'] = 'Cadastrar Pedido'
        context['botao'] = 'Cadastrar'
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']

        if form.is_valid() and formset.is_valid():
            form.instance.criado_por = self.request.user
            form.instance.data_pedido = datetime.now() 
            self.object = form.save()

            formset.instance = self.object
            formset.save()

            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))

    
class PedidoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Pedido
    fields = ['nome', 'cliente', 'data_entrega', 'valor_adiantado', 'valor_total', 'status']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-pedido')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.POST:
            context['formset'] = ProdutoPedidoFormSet(self.request.POST, instance=self.object)
        else:
            context['formset'] = ProdutoPedidoFormSet(instance=self.object)

        context['titulo'] = 'Editar Pedido'
        context['botao'] = 'Atualizar'

        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']

        # Verifica se tanto o form do Pedido quanto o formset dos Produtos são válidos
        if form.is_valid() and formset.is_valid():
            # Atualiza o Pedido
            form.instance.criado_por = self.request.user
            self.object = form.save()

            # Atualiza o formset (produtos do pedido)
            formset.instance = self.object
            formset.save()

            return super().form_valid(form)
        else:
            # Se o form ou formset for inválido, renderiza novamente o template com os erros
            return self.render_to_response(self.get_context_data(form=form))


    
class PedidoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Pedido
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-pedido')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Excluir Pedido'
        context['botao'] = 'Excluir'
        
        return context
    
class PedidoList(LoginRequiredMixin, FilterView):
    login_url = reverse_lazy('login')
    model = Pedido
    template_name = 'cadastros/listas/pedido.html'
    context_object_name = 'pedidos'
    filterset_class = PedidoFilter

#endregion Pedido

#region Produto

class ProdutoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Produto
    fields = ['nome', 'categoria', 'preco']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-produto')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastrar Produto'
        context['botao'] = 'Cadastrar'
        
        return context
    
    def form_valid(self, form):
        # Antes do super não foi criado o objeto no banco
        form.instance.criado_por = self.request.user
        form.instance.data_cadastro = datetime.now()
        
        url =  super().form_valid(form)
        
        # Depois do super o objeto já foi criado no banco
        #self.object.observacao += " - Criado por: {}".format(self.request.user)
        #self.object.save()
        
        return url
    
class ProdutoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Produto
    fields = ['nome', 'categoria', 'preco']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-produto')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Produto'
        context['botao'] = 'Atualizar'
        
        return context
    
class ProdutoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Produto
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-produto')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Excluir Produto'
        context['botao'] = 'Excluir'
        
        return context

class ProdutoList(LoginRequiredMixin, FilterView):
    login_url = reverse_lazy('login')
    model = Produto
    template_name = 'cadastros/listas/produto.html'
    context_object_name = 'produtos'
    filterset_class = ProdutoFilter

#endregion Produto

#region ProdutoPedido

class ProdutoPedidoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = ProdutoPedido
    fields = ['produto', 'quantidade', 'descricao_personalizada']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-produto-pedido')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastrar Produto Pedido'
        context['botao'] = 'Cadastrar'
        
        return context
    
    def form_valid(self, form):
        # Antes do super não foi criado o objeto no banco
        form.instance.data_cadastro = datetime.now()
        
        url =  super().form_valid(form)
        
        return url
    
class ProdutoPedidoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = ProdutoPedido
    fields = ['produto', 'quantidade']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-produto-pedido')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Produto Pedido'
        context['botao'] = 'Atualizar'
        
        return context
    
class ProdutoPedidoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = ProdutoPedido
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-produto-pedido')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Excluir Produto Pedido'
        context['botao'] = 'Excluir'
        
        return context
    
class ProdutoPedidoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = ProdutoPedido
    template_name = 'cadastros/listas/produto-pedido.html'
    context_object_name = 'produtos_pedido'

#endregion ProdutoPedido

#region Cliente

class ClienteCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Cliente
    fields = ['nome', 'telefone', 'endereco']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-cliente')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastrar Cliente'
        context['botao'] = 'Cadastrar'
        
        return context
    
    def form_valid(self, form):
        form.instance.criado_por = self.request.user
        form.instance.data_cadastro = datetime.now()
        
        url =  super().form_valid(form)
            
        return url
    
class ClienteUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Cliente
    fields = ['nome', 'telefone', 'endereco']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-cliente')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Cliente'
        context['botao'] = 'Atualizar'
        
        return context
    
class ClienteDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Cliente
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-cliente')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Excluir Cliente'
        context['botao'] = 'Excluir'
        
        return context
    
class ClienteList(LoginRequiredMixin, FilterView):
    login_url = reverse_lazy('login')
    model = Cliente
    template_name = 'cadastros/listas/cliente.html'
    context_object_name = 'clientes'
    filterset_class = ClienteFilter


#endregion Cliente