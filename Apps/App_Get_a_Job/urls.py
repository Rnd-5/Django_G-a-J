from django.conf.urls import url
from .views import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate

urlpatterns = [
    url(r'^home/$', login_required(home), name='home'),
    url(r'^Log', Log, name='Log'),
    url(r'^PerfilSolct/$', login_required(PerfilSolct), name='PerfilSolct'),
    url(r'^PagP', login_required(PagP), name='PagP'),
    url(r'^c_Oferta', login_required(crearOferta), name='c_Oferta'),
    url(r'^p_Solicitante', login_required(PerfilSolct), name='p_Solicitante'),
    url(r'^l_Solicitante/', login_required(l_Solicitante.as_view()), name='l_Solicitante'),
    url(r'^l_curriculum/', login_required(l_curriculum.as_view()), name='l_curriculum'),
    #url(r'^n_C/', curriulum_view, name='n_C')
]

