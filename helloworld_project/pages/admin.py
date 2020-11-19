from django.contrib import admin
from .models import Autor, Publicacion

# Register your models here.
admin.site.register(Autor)
admin.site.register(Publicacion)