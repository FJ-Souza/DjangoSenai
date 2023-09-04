from django.db import models

# Create your models here.
class Banner(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    path = models.ImageField(upload_to='imagem/site/')
    
class ConteudoMain(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    
class CardProduct(models.Model):
    name = models.CharField(max_length=40)
    price = models.FloatField()
    description = models.CharField(max_length=255)
    path = models.ImageField(upload_to='imagem/site/')
    
class ConteudoSegundoMain(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    path = models.ImageField(upload_to='imagem/site/')
    
class CardSegundoMain(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    path = models.ImageField(max_length=255)
    
class ConteudoTerceiroMain(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    
class CardTerceiroMain(models.Model):
    description = models.CharField(max_length=255)
    
class Testemunho(models.Model):
    name = models.CharField(max_length=255)
    cargo = models.CharField(max_length=80)
    description = models.CharField(max_length=255)
    path = models.ImageField(upload_to='imagem/site/')
    
class Blog(models.Model):
    title = models.CharField(max_length=255)
    path = models.ImageField(upload_to='imagem/site/')
    
class Footer(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    path = models.ImageField(upload_to='imagem/site/')
    
class CardTerceiro(models.Model):
    path = models.ImageField(upload_to='imagem/site/')