from django.db import models

# Create your models here.
class Project(models.Model): #Con esta clase creamos los campos para agregar nuevos 'POST', y traducimos el menú
    title = models.CharField(max_length=200, verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripcion")
    image = models.ImageField(verbose_name="Imagen", upload_to="Project")
    link = models.URLField(null=True, blank=True, verbose_name="Direccion Web")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    update = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta: #Con esta clase traducimos la seccion de nuestra app 
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"
        ordering = ("-created",)

    def __str__(self): #Esta funcion nos muestra el titulo en la vista previa
        return self.title