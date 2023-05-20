from django.db import models
# from django.utils import timezone
# from django.utils.translation import gettext_lazy

class Products(models.Model):
    productCategory = models.CharField(max_length=10)
    productName = models.CharField(max_length=20)
    productCost = models.IntegerField(blank=False , null= False )
    productImage = models.ImageField(upload_to = 'productImages',max_length = 250, null = True,default = None)
    productDescription = models.TextField()

    def __str__(self):
        return self.productName


# class NewUser():
#     email = models.EmailField(gettext_lazy ('email address '), unique = True)
#     user_name = models.CharField(max_length = 150 , unique = True)
#     first_name = models.CharField(max_length = 150 )
#     last_name = models.CharField(max_length = 150)
#     start_date = models.DateTimeField(default = timezone.now)
#     about = models.TextField(gettext_lazy('about'), max_length = 500 , blank = True)
#     is_staff = models.BooleanField(default = False)
#     is_active = models.BooleanField(default = False)

#     def __str__(self):
#         return self.user_name
