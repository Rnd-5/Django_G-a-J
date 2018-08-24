from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, logout_then_login, login_required
from Apps.App_Get_a_Job.views import home


urlpatterns = [
    url(r'^$', login_required(home), name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^App_Get_a_Job/', include('Apps.App_Get_a_Job.urls', namespace='App_Get_a_Job')),
    url(r'^accounts/login', login, {'template_name': 'App_G_a_J/Login_Registro.html'}, name='login'),
    url(r'^logout/', logout_then_login, name='logout'),
    url(r'^App_Get_a_Job/', include('Apps.App_Get_a_Job.urls', namespace='App_Get_a_Job')),
]
