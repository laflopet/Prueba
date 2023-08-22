from django.db import models

# Create your models here.
class Propietario(models.Model):
    TIPOS_IDENTIFICACION = [
        ('CC', 'Cédula de ciudadanía'),
        ('CE', 'Cédula de extranjería'),
        ('NIT', 'Número de identificación tributaria'),
        ('TI', 'Tarjeta de Identidad'),
    ]

    TIPOS_PROPIETARIO = [
        ('Natural', 'Natural'),
        ('Juridica', 'Juridica'),
    ]

    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=10, choices=TIPOS_PROPIETARIO)
    numero_identificacion = models.CharField(max_length=20, unique=True)
    tipo_identificacion = models.CharField(max_length=3, choices=TIPOS_IDENTIFICACION)


class Predio(models.Model):
    TIPOS_PREDIO = [
        ('Urbano', 'Urbano'),
        ('Rural', 'Rural'),
    ]

    nombre_direccion = models.CharField(max_length=200)
    tipo_predio = models.CharField(max_length=10, choices=TIPOS_PREDIO)
    numero_catastral = models.CharField(max_length=30, unique=True)
    numero_matricula_inmobiliaria = models.CharField(max_length=30, unique=True)
    propietarios = models.ManyToManyField(Propietario, related_name='predios')
