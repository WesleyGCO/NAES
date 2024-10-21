# forms.py
# forms.py
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Row, Column
from django.forms.models import inlineformset_factory
from .models import Pedido, ProdutoPedido

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['nome', 'cliente', 'data_entrega', 'valor_adiantado', 'valor_total', 'status']
        widgets = {
            'data_entrega': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Salvar Pedido'))


class ProdutoPedidoForm(forms.ModelForm):
    class Meta:
        model = ProdutoPedido
        fields = ['produto', 'quantidade']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        
class BaseProdutoPedidoFormSet(forms.BaseInlineFormSet):
    def add_fields(self, form, index):
        super().add_fields(form, index)
        if self.instance.pk:
            if form.instance.pk is None:
                form.fields['produto'].initial = None
                form.fields['quantidade'].initial = 0    

ProdutoPedidoFormSet = inlineformset_factory(
    Pedido,
    ProdutoPedido,
    fields=['produto', 'quantidade'],
    extra=1,
    can_delete=True,
    formset=BaseProdutoPedidoFormSet
)