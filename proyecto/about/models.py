from django.db import models

# Create your models here.
class About(models.Model):
    name = models.CharField(max_length=30, verbose_name="Nombre")
    parrafo_1 = models.TextField(verbose_name="Primer Parrafo")
    parrafo_2 = models.TextField(verbose_name="Segundo Parrafo")
    image = models.ImageField(verbose_name="Imagen", upload_to="Proyect")

    class Meta:
        verbose_name = "Acerca De"
        verbose_name_plural = "Acerca De"