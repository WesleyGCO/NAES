from django.views.generic import TemplateView

# Create your views here.
class IndexView(TemplateView): # class Index extends TemplateView (herança)
    template_name = "paginas/index.html"