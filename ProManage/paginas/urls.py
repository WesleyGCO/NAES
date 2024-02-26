from django.urls import path
from .views import IndexView

urlpatterns = [
    #path("rota/", suaView, name="pagina-inicial")
    path("inicio/", IndexView.as_view(), name = 'index'),
]
