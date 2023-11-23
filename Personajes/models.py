from django.db import models

#Campos clase Sailor Moon
class Sailor(models.Model):
    categoria = models.CharField(max_length=6)
    nombre = models.CharField(max_length=10)
    planeta = models.CharField(max_length=50)
    objeto = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.nombre} - Categoría: {self.categoria}"
    
#Campos clase Club Winx
class Winx(models.Model):
    categoria = models.CharField(max_length=6)
    nombre = models.CharField(max_length=10)
    tipohada = models.CharField(max_length=50)
    transformacion = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.nombre} - Categoría: {self.categoria}"
    
#Campos clase W.I.T.C.H
class Witch(models.Model):
    categoria = models.CharField(max_length=6)
    nombre = models.CharField(max_length=10)
    elemento = models.CharField(max_length=50)
    signo = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.nombre} - Categoría: {self.categoria}"