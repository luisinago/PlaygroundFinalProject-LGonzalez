from django.db import models
from django.contrib.auth.models import User

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)
    descripcion = models.TextField(null=True)
    link = models.URLField(null=True)
    
    def __str__(self):
        return f"{self.user} - {self.imagen}"
