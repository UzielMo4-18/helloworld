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

#Modelo de comentarios
class Comentario(models.Model):
    autor_comentario=models.ForeignKey(Autor,on_delete=models.CASCADE)
    fecha_comentario=models.DateField()
    contenido_comentario=models.CharField(max_length=125)
    id_publicacion=models.ForeignKey(Publicacion,on_delete=models.CASCADE)
    reaccion=models.IntegerField()

    def __str__(self):
        return self.contenido_comentario