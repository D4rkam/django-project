from django.db import models

# Create your models here.
<<<<<<< HEAD
class Contact(models.Model):
    num_telefono = models.BigIntegerField(verbose_name="Número de telefono", null=False)
    descripcion_tel = models.CharField(max_length=200, verbose_name="Pequeña descripción", null=False)
    email = models.EmailField(verbose_name="Email", null=False)
    descripcion_email = models.CharField(max_length=200, verbose_name="Pequeña descripción", null=False)
    num_whatsapp = models.BigIntegerField(verbose_name="Número de Whatsapp", null=False)
    descripcion_whatsapp = models.CharField(max_length=200, verbose_name="Pequeña descripción", null=False)

    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"
    
    def __str__(self):
        return "Contacto"
=======
>>>>>>> 7aa53a6dd013dc37f354cf930508aa4e74b902c0
