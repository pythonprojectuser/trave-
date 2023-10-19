from django.db import models
from django.http import HttpResponse


# Create your models here.
class Carlist(models.Model):
    name=models.CharField(max_length=250)
    mnum=models.IntegerField()
    desc=models.TextField()
    year=models.IntegerField()
    img=models.ImageField()
    def __str__(self):
       return self.name
