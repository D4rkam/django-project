from django.db import models

# Create your models here.
class About(models.Model):
    name = models.CharField(max_length=30, verbose_name="Nombre")
    parrafo_1 = models.TextField(verbose_name="Primer Parrafo")
    parrafo_2 = models.TextField(verbose_name="Segundo Parrafo")
    image = models.ImageField(verbose_name="Foto de Perfil", upload_to="Proyect")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    update = models.DateTimeField(auto_now=True, verbose_name="Fecha de Actualización")

    class Meta:
        verbose_name = "Acerca De"
        verbose_name_plural = "Acerca De"
        ordering = ("-created",)
    
    def __str__(self):
        return self.name