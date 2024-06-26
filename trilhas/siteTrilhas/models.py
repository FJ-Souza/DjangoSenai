from datetime import datetime
from django.db import models

# Create your models here.
class Site(models.Model):
    nome_card = models.CharField(max_length=200)
    description =  models.TextField()
    primeiro_texto = models.TextField()
    segundo_texto = models.TextField()
    alunos = models.IntegerField()
    date_create = models.DateTimeField(default=datetime.now, blank =True)
    path = models.ImageField(upload_to='photos/%Y/%m/%d/')