from django.shortcuts import render, render_to_response
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required()
def imageGallery(request):
    imagenes = Imagen.objects.all()
    return render_to_response('images.html',  {'usuario':request.user, 'imagenes':imagenes})

@login_required()
def videoGallery(request):
    return render_to_response('video.html')

@login_required()
def musicGallery(request):
    return render_to_response("music.html")

@login_required()
def albumGallery(request):
    return render_to_response("images.html")


def userView(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = Usuario

    return render_to_response('index.html', locals())