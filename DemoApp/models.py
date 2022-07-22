from django.db import models

class Products(models.Model):
    productCategory = models.CharField(max_length=10)
    productName = models.CharField(max_length=20)
    productCost = models.IntegerField(blank=False , null= False )
    productImage = models.ImageField(upload_to = 'productImages',max_length = 250, null = True,default = None)
    productDescription = models.TextField()

    def __str__(self):
        return self.productName
