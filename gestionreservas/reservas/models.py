from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=500, verbose_name="Nombre")
    direccion = models.TextField(max_length=1000,verbose_name="Direccion")
    pais = models.CharField(max_length=50, verbose_name="Pais")

    class Meta:
        verbose_name  = 'Persona'
        verbose_name_plural  = 'Personas'
        ordering = ['-nombre']

    def _str_(self):
        return self.nombre
    

class Habitacion(models.Model):
    tipo = models.CharField(max_length=50, verbose_name="Tipo de Habitacion")
    numero_maximo_personas = models.IntegerField(null=False, verbose_name="Numero maximo de personas")
    precio = models.IntegerField(null=False, verbose_name="Precio")
    imagen = models.ImageField(verbose_name="Imagen", upload_to="habitaciones")
    # persona= models.OneToOneField("Persona",null=True, on_delete=models.SET_NULL,verbose_name="Persona")

    class Meta:
        verbose_name  = 'Habitacion'
        verbose_name_plural  = 'Habitaciones'
        ordering = ['-tipo']

    def __str__(self):
        return self.tipo