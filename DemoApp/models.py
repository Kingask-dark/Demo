from operator import mod
from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.
class Products(models.Model):
    productCategory = models.CharField(max_length=10)
    productName = models.CharField(max_length=20)
    productCost = models.IntegerField(blank=False , null= False )
    productImage = models.ImageField(upload_to = None)
    productDescription = models.TextField()

