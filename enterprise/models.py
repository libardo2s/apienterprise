from django.db import models


# Create your models here.
class Enterprise(models.Model):
    name = models.CharField('Nombre empresa', max_length=100)
    address = models.CharField('Direccion', max_length=50)
    nit = models.CharField('NIT', max_length=50, unique=True)
    phone = models.CharField('Telefono', max_length=10)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
