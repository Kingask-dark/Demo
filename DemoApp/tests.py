from django.test import TestCase
from DemoApp.models import Products

# Create your tests here.

class ProductModelTest(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        Products.objects.create(productCategory= "Beer",productName = "Test",productCost = 10,productImage = "D:\Django\bestbeers-pliny-843736092.jpg",productDescription = "This is a unit testing")
        return super().setUpClass()
    
    def test_productCategory(self):
        product = Products.objects.get(id = 1)
        field_label = product._meta.get_field('productCategory').verbose_name
        self.assertEqual(field_label,'productCategory')
    
    def test_productName(self):
        product = Products.objects.get(id = 1)
        field_label = product._meta.get_field('productName').verbose_name
        self.assertEqual(field_label,'productName')


    def test_productCost(self):
        product = Products.objects.get(id = 1)
        field_label = product._meta.get_field('productCost').verbose_name
        self.assertEqual(field_label,'productCost')

    def test_productImage(self):
        product = Products.objects.get(id = 1)
        field_label = product._meta.get_field('productImage').verbose_name
        self.assertEqual(field_label,'productImage')

    def test_productDescription(self):
        product = Products.objects.get(id = 1)
        field_label = product._meta.get_field('productDescription').verbose_name
        self.assertEqual(field_label,'productDescription')