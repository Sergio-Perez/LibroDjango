from django.urls import include,path,re_path

from . import views


app_name = "biblioteca_app"

urlpatterns = [ 
    path("", views.ListaAutores.as_view() , name = "lista-autores"),
    path("libros-autor/<pk>/por-autor", views.ListaLibrosAutores.as_view() , name = "lista-libros"),
    path("autor/add", views.AddAutor.as_view() , name = "autor-add"),

]