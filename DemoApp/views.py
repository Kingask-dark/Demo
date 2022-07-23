from itertools import product
from django.shortcuts import render
from django.http import HttpResponse
from DemoApp.models import Products
# Create your views here.
def temp(req):
    detail = Products.objects.all().order_by('?')
    # print("the details ----> ", detail.values())
    return render(req,'DemoApp/index.html',{'detail':detail})

def wine(req):
    detail = Products.objects.filter(productCategory = 'Wine').order_by('?')
    return render(req, 'DemoApp/products/wine.html',{'detail':detail})

def beer(req):
    detail = Products.objects.filter(productCategory = 'Beer').order_by('?')
    return render(req, 'DemoApp/products/beer.html',{'detail':detail})

def champagne(req):
    detail = Products.objects.filter(productCategory = 'Champagne').order_by('?')
    return render(req, 'DemoApp/products/champagne.html',{'detail':detail})

def vodka(req):
    detail = Products.objects.filter(productCategory = 'Vodka').order_by('?')
    return render(req, 'DemoApp/products/vodka.html',{'detail':detail})
