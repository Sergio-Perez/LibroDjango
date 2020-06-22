from django.contrib import admin

# Register your models here.
from .models import Autor,Libros

# Clase mejorar administrador autor

class AutorAdmin(admin.ModelAdmin):
    list_display =[
        "nombre",
        "nacionalidad",
        "id"
    ]
    # atributo buscar por un campo
    search_fields = ("nombre","nacionalidad")



class LibrosAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "resume",
        "autor",
        "id",
    ]
    
    # atributo buscar por un campo
    search_fields = ("title",)
    # para filtros
    
    list_filter = ("autor",)

admin.site.register(Autor, AutorAdmin)
admin.site.register(Libros, LibrosAdmin)