from django.views.generic import TemplateView

from cadastros.models import Pedido

# Create your views here.

class IndexView(TemplateView):
    template_name = 'paginas/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['titulo'] = 'Página inicial'
        context['pedidos'] = Pedido.objects.all().count()
        
        return context
    
class SobreView(TemplateView):
    template_name = 'paginas/sobre.html'
    
class LoginView(TemplateView):
    template_name = 'paginas/login.html'