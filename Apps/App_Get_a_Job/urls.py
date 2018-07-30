from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^home/', home, name='home'),
    url(r'^c_Solicitante', crearSolicitante, name='c_Solicitante'),
    url(r'^c_Empleador', crearEmpleador, name='c_Empleador'),
    url(r'^c_Oferta', crearOferta, name='c_Oferta')
]