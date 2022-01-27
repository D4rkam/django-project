from tabnanny import verbose
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class About(models.Model):
    name = models.CharField(max_length=30, verbose_name="Nombre", null=False)
    profesion = models.CharField(max_length=50, verbose_name="Profesión", null=False)
    parrafo = RichTextField(verbose_name="Parrafos", null=False)
    image = models.ImageField(verbose_name="Foto de Perfil", upload_to="Project", null=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    update = models.DateTimeField(auto_now=True, verbose_name="Fecha de Actualización")

    class Meta:
        verbose_name = "Acerca De"
        verbose_name_plural = "Acerca De"
    
    def __str__(self):
        return self.name