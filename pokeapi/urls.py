"""pokeapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from pokeapi.views import ver_todos,ver_uno, ver_tipo

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', ver_todos, name='ver_todos'),
    url(r'^ver_uno/(?P<nombre_pokemon>[^/]+)/(?P<id_pokemon>[^/]+)/$', ver_uno, name='ver_uno'),
   url(r'^ver_tipo/(?P<id_tipo>[^/]+)/$', ver_tipo, name='ver_tipo'),
]
