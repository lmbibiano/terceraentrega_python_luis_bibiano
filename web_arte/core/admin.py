from django.contrib import admin
from .models import Curso, Historial, Artista

# Register your models here.
# modelos registrados en el administrador
admin.site.register(Curso)
admin.site.register(Historial)
admin.site.register(Artista)
