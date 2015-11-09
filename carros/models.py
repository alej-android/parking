from django.db import models

class Carros(models.Model):
    lote = models.CharField(max_length = 5)
    placas = models.CharField(max_length =15)
    marca = models.CharField(max_length =20)
    modelo = models.CharField(max_length = 25)
    tipo = models.CharField(max_length = 15)
    color = models.CharField(max_length = 10)
    anio = models.CharField(max_length = 4)

    def __str__(self):
        return self.placas+" "+self.marca+" "+self.color
