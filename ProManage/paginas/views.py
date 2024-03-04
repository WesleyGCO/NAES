from django.views.generic import TemplateView

# Create your views here.
class IndexView(TemplateView): # class Index extends TemplateView (herança)
    template_name = "paginas/index.html"


class SobreView(TemplateView):
    template_name = "paginas/sobre.html"