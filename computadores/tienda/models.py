from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Categoria(models.Model):
    id_categoria    = models.BigAutoField(db_column='idCategoria', primary_key=True)
    descripcion     = models.CharField(max_length=25)
    
    def __str__(self):
        return str(self.descripcion)

class Producto(models.Model):
    id_producto     = models.BigAutoField(db_column='idProducto', primary_key=True)
    id_categoria    = models.ForeignKey('Categoria', on_delete=models.CASCADE, db_column='idCategoria')
    nombre          = models.CharField(max_length=25)
    marca           = models.CharField(max_length=25)
    descripcion     = models.CharField(max_length=200)
    precio          = models.IntegerField()
    stock           = models.IntegerField()
    imagen          = models.ImageField(upload_to='productos/', null=True)

    def __str__(self):
        return "ID: "+str(self.id_producto)+" "+str(self.nombre)+" /"+str(self.id_categoria)

class Usuario(models.Model):#Tomar como referencia tabla usuari clienteos
    username        = models.CharField (max_length=20, primary_key=True)
    pnombre         = models.CharField (max_length=15)
    appaterno       = models.CharField (max_length=15)
    email           = models.EmailField(unique=True, max_length=60)
    contrasena      = models.CharField (max_length=20)
    direccion       = models.CharField (max_length=50)
    celular         = models.CharField (max_length=9)

    def __str__(self):
        return str(self.rut)+" "+str(self.pnombre)+" "+str(self.appaterno)

