from django.contrib import admin
from .models import Usuario, Album, Imagen, Evento, Familiar, Keyword
from .forms import UserForm

# Register your models here.

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
     form = UserForm
     list_display = [Usuario.get_full_name,]

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    fields = ['titulo','descripcion','thumbnail','evento','usuario']
    date_hierarchy = 'fecha_creacion'

@admin.register(Imagen)
class ImagenAdmin(admin.ModelAdmin):
    list_display = ('titulo',)

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    pass

@admin.register(Keyword)
class KeywordAdmin(admin.ModelAdmin):
    list_display = ('keyword',)
    ordering = ('keyword',)