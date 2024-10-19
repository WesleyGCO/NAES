from django.urls import path
from .views import IndexView, SobreView, LoginView

urlpatterns = [
    path('inicio/', IndexView.as_view(), name='inicio'),
    path('sobre/', SobreView.as_view(), name='sobre'),
]