from django.db import models

class Sensos(models.Model):
    name = models.CharField(max_length=50)
    occupation = models.CharField(max_length=50)
     
