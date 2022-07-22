from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def temp(req):
    return render(req,'DemoApp/index.html')

def signin(req):
    return render(req, 'DemoApp/signin.html')

def wine(req):
    return render(req, 'DemoApp/products/wine.html')

def beer(req):
    return render(req, 'DemoApp/products/beer.html')

def champagne(req):
    return render(req, 'DemoApp/products/champagne.html')

def vodka(req):
    return render(req, 'DemoApp/products/vodka.html')
