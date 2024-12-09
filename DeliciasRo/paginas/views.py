from django.views.generic import TemplateView
from datetime import datetime, timedelta

from django_filters.views import FilterView

from cadastros.models import Pedido

# Create your views here.

class IndexView(TemplateView):
    template_name = 'paginas/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = datetime.today()
        
        # Ajuste para considerar o domingo como parte da nova semana
        if today.weekday() == 6:  # Domingo
            sunday = today
        else:
            sunday = today - timedelta(days=today.weekday() + 1)
        
        # Calcula o sábado (final da semana)
        saturday = sunday + timedelta(days=6)

        # Formata as datas no formato desejado
        context['data_inicial'] = sunday.strftime('%d-%m')
        context['data_final'] = saturday.strftime('%d-%m')
        
        # Filtra pedidos pendentes pela data de entrega
        context['pedidos_pendentes'] = Pedido.objects.filter(
            status='Pendente',
            data_entrega__date__gte=sunday,
            data_entrega__date__lte=saturday
        )

        context['titulo'] = 'Página inicial'
        context['pedidos'] = Pedido.objects.all().count()

        return context
    
class SobreView(TemplateView):
    template_name = 'paginas/sobre.html'
    
class LoginView(TemplateView):
    template_name = 'paginas/login.html'