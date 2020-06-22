from django.shortcuts import render

from django.views.generic import ( 
    TemplateView,
    ListView,
    )
# Create your views here.

class IndexView(TemplateView):
    # una vista procesa los datos y renderiza el resultado en pantalla
    # siempre nos pedira un tempalate para trabajar
    # un template es un archivo html
    template_name = "home/index.html"


class ListaLibros(ListView):
    template_name = "home/lista.html"
    queryset = ["Harry Potter","El quijote","La que me dio un beso","Veamos lo que tengo","Django 2.0"]
    context_object_name = "libros"