from django.shortcuts import render

# Create your views here.

from django.views.generic import ( 
    TemplateView,
    ListView,
    CreateView,
    )
from .models import Autor, Libros
# Create your views here.



class ListaAutores(ListView):
    template_name = "biblioteca/lista-autores.html"
    model = Autor
    context_object_name = "autores"

# Lista libros por autoe
class ListaLibrosAutores(ListView):
    template_name = "biblioteca/lista-libros.html"
    context_object_name = "libros" 

    def get_queryset(self):
      
        # identificar el autor
        id = self.kwargs["pk"]
        
        # Filtro libros
        lista = Libros.objects.filter(
            autor = id
        )

        # Filtro por nacionalidad
        #nac = self.kwargs['nacionalidad']
        #lista = Libros.objects.filter(
        #    autor__nacionalidad = nac
        #)
        # Resultado
        return lista


class AddAutor(CreateView):
    """ vista para registrar un n uevo autor """
    template_name = "biblioteca/add-autor.html"
    model = Autor
    # que campos quiero que visite para que se pueda registrar
    fields = ["nombre","nacionalidad"] # Para validar otro tipo de fields que es distinto

    success_url = "/" # recarge la pagina que yo elija

