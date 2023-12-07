from django import forms

# escribir formularios


# Estos son los formularios hechos por el usuario
class ArteFormulario(forms.Form):
    titulo = forms.CharField(max_length=40)
    url = forms.URLField()


class HistoriaFormulario(forms.Form):
    titulo = forms.CharField(max_length=40)
    url = forms.URLField()


class ArtistaFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    url = forms.URLField()
