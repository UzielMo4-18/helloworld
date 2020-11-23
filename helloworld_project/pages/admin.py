from django.contrib import admin
from .models import Autor, Publicacion, Comentario

# Register your models here.
admin.site.register(Autor)
admin.site.register(Publicacion)
admin.site.register(Comentario)