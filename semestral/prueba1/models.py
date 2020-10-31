from django.db import models

# Create your models here.

class Cliente(models.Model):
    name= models.CharField(max_length=80, primary_key=True)
    apellido= models.CharField(max_length=80)
    email= models.CharField(max_length=35)
    username= models.CharField(max_length=8)
    password= models.CharField(max_length=8)

    def __str__(self):
        return self.name


class Insumos(models.Model):
    name= models.CharField(max_length=80, primary_key=True)
    precio= models.IntegerField()
    descripcion= models.TextField(null=True)
    stock= models.IntegerField()

    def __str__(self):
        return self.name


class SliderHindex(models.Model):
    ident = models.CharField(max_length=20,primary_key=True)
    imagen = models.ImageField(upload_to='autos', null=True)

    def __str__(self):
        return self.ident

class MisionVision(models.Model):
    ident = models.CharField(max_length=20,primary_key=True)
    mision = models.TextField()
    vision = models.TextField()

    def __str__(self):
        return self.ident

class Galeria(models.Model):
    ident = models.CharField(max_length=20,primary_key=True)
    imagen = models.ImageField(upload_to='autos',null=True)

    def __str__(self):
        return self.ident