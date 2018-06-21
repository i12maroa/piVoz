from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
# Create your models here.

class Usuario(AbstractUser):
    telefono = PhoneNumberField()


class Familiar(Usuario):
    is_staff = True

class Evento(models.Model):
    id_evento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80, unique=True)
    ubicacion = models.CharField(max_length=80)
    fecha_evento = models.DateTimeField()

    class Meta:
        verbose_name_plural = "Eventos"

    def __str__(self):
        return self.nombre

class Album(models.Model):
    image_height = models.PositiveSmallIntegerField(default=400)
    image_width = models.PositiveSmallIntegerField(default=400)
    id_album = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=40, null=False, default=str(datetime.now()))
    descripcion = models.TextField(verbose_name='Descripción del Álbum', blank=True)
    thumbnail = models.ImageField(upload_to='thumbs', height_field='image_height', width_field='image_width')
    fecha_creacion = models.DateTimeField(verbose_name='Fecha de creación',auto_now_add=True)
    fecha_modificacion = models.DateTimeField(verbose_name='Última edición', auto_now=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    #familiar = models.ForeignKey(Familiar, on_delete=models.CASCADE, related_name="Administrador")
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name_plural = "Álbumes"

class Multimedia(models.Model):
    id_multimedia = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=80, default='image'+str(datetime.now()))
    descripción = models.TextField(blank=True, help_text='Descríbeme...')
    path = models.FilePathField(path='media',allow_folders=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    keyword = models.ManyToManyField('Keyword', help_text= "Selecciona las Personas que aparezcan en la foto.")

    def __str__(self):
        return self.titulo

class Imagen(Multimedia):
    image_width = models.PositiveSmallIntegerField(default=640)
    image_height = models.PositiveSmallIntegerField(default=480)
    fichero_imagen = models.ImageField(verbose_name='Archivo de imagen',
                               upload_to='files/img',
                               width_field='image_width',
                               height_field='image_height')
    thumbnail = ImageSpecField(source='fichero_imagen',
                               processors=[ResizeToFill(600, 300)],
                               format='JPEG',
                               options={'quality': 60})

    class Meta:
        verbose_name_plural = "Imágenes"


class Keyword(models.Model):
    id_keyword = models.AutoField(primary_key=True)
    keyword = models.CharField(max_length=200, unique=True,)

    def __str__(self):
        return self.keyword








