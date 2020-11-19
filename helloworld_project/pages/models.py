from django.db import models

# Create your models here.

#Modelo de autor
class Autor(models.Model):
    nombre=models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

#Modelo de publicaciones
class Publicacion(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=250)
    fecha_creacion=models.DateField()
    autor=models.ForeignKey(Autor,on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo