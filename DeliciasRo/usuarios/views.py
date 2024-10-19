from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .forms import UsuarioForm

# Create your views here.
class UsuarioCreate(CreateView):
    template_name = "cadastros/form.html"
    success_url = reverse_lazy('login')
    form_class = UsuarioForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de Usuário'
        context['botao'] = 'Cadastrar'
        
        return context