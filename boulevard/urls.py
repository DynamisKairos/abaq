# -*- coding: utf-8 -*-
"""boulevard URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^chaining/', include('smart_selects.urls')),
]
# Texto para poner al final del <title> de cada página.
admin.site.site_title = u'Dynamis Kairos C.A.'

# Texto a poner en los <h1> de todas las páginas.
admin.site.site_header = u'Sitio de administración'

# Texto a poner arriba de la página de index del admin
admin.site.index_title = u'Panel de control empresarial'
