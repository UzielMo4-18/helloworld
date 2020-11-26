from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Publicacion, Autor, Comentario

# Create your views here.

class home(View):
    def get(self,request):
        publicaciones=Publicacion.objects.all()
        comentarios=Comentario.objects.all()
        #for pub in publicaciones: print(pub)
        context={'publicaciones':publicaciones,'comentarios':comentarios}
        #contextC={'comentarios':comentarios}
        return render(request,'index.html',context)