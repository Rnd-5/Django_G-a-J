from django.conf.urls import url
from .views import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate

urlpatterns = [
    url(r'^home/', home, name='home'),
    url(r'^login', login, name='login'),
    url(r'^c_Solicitante', crearSolicitante, name='c_Solicitante'),
    url(r'^c_Empleador', crearEmpleador, name='c_Empleador'),
    url(r'^c_Oferta', login_required(crearOferta), name='c_Oferta'),
    url(r'^PagP/', login_required(PagP), name='PagP'),
    url(r'^l_Solicitante/', list_Solicitantes, name='l_Solicitante'),
    #url(r'^c_Usuario/', CrearUsuario.as_view(), name='c_Usuario'),
]

