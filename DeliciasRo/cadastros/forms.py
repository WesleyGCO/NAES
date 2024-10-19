# forms.py
from django import forms
from django.forms import inlineformset_factory
from .models import Pedido, ProdutoPedido

class ProdutoPedidoForm(forms.ModelForm):
    class Meta:
        model = ProdutoPedido
        fields = ['produto', 'quantidade']

ProdutoPedidoFormSet = inlineformset_factory(Pedido, ProdutoPedido, form=ProdutoPedidoForm, extra=1)