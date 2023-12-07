"""
URL configuration for web_arte project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.arteFormulario, name="curso"),
    path("historia/", views.historiaFormulario, name="historia"),
    path("artista/", views.artistaFormulario, name="artista"),
    path("busquedaCurso/", views.busquedaCurso, name="busquedaCurso"),
    path("buscar/", views.buscar),
    path("busquedaHistoria/", views.busquedaHistoria, name="busqueda_historia"),
    path("buscar-historia/", views.buscar_historia, name="buscar_historia"),
    path("busquedaArtista/", views.busquedaArtista, name="busqueda_artista"),
    path("buscar-artista/", views.buscar_artista, name="buscar_artista"),
]
