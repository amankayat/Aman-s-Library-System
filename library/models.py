from django.db import models

# Create your models here.
class books(models.Model):
    name = models.CharField(max_length=200)
    subject = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publish =models.DateField()