from django.db import models

# Create your models here.
class product(models.Model):
    name=models.CharField(max_length=200)
    product=models.CharField(max_length=100)
    