"""Proyecto_Final_DS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, logout_then_login
from Apps.App_Get_a_Job.views import home
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^App_Get_a_Job/', include('Apps.App_Get_a_Job.urls', namespace='App_Get_a_Job')),
    url(r'^accounts/login', login, {'template_name': 'App_G_a_J/Login_Registro.html'}, name='login'),
    url(r'^logout/', logout_then_login, name='logout'),
    url(r'^App_Get_a_Job/', include('Apps.App_Get_a_Job.urls', namespace='App_Get_a_Job')),
]
