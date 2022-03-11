from django.urls import path
from .views import inicio, otra_vista, numero_del_usuario, numero_random

urlpatterns = [
    path("inicio/", inicio),
    path("", otra_vista),
    path("random/", numero_random),
    path("dame-numero/<int:numero>", numero_del_usuario),
]
