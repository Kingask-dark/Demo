from django.shortcuts import redirect, render
from DemoApp.models import Products
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def temp(req):
    # return redirect('/logIn/')
    detail = Products.objects.all().order_by('?')
    userDetails = req.user
    # print("the details ----> ", detail.values())
    return render(req, 'DemoApp/index.html', {'detail': detail , 'userDetails': userDetails})


def wine(req):
    detail = Products.objects.filter(productCategory='Wine').order_by('?')
    userDetails = req.user
    print(userDetails)
    return render(req, 'DemoApp/products/wine.html', {'detail': detail , 'userDetails': userDetails})


def beer(req):
    detail = Products.objects.filter(productCategory='Beer').order_by('?') 
    userDetails = req.user
    return render(req, 'DemoApp/products/beer.html', {'detail': detail , 'userDetails': userDetails})


def champagne(req):
    detail = Products.objects.filter(productCategory='Champagne').order_by('?')
    userDetails = req.user
    return render(req, 'DemoApp/products/champagne.html', {'detail': detail , 'userDetails': userDetails})


def vodka(req):
    detail = Products.objects.filter(productCategory='Vodka').order_by('?')
    userDetails = req.user
    return render(req, 'DemoApp/products/vodka.html', {'detail': detail , 'userDetails': userDetails})


def details(req,product_id ,product_name):
    detail = Products.objects.get(id=product_id ,productName = product_name )
    userDetails = req.user
    return render(req, 'DemoApp/detail.html', {'product': detail,'userDetails': userDetails})

def signUp(req):

    if req.method == "POST":
        fName = req.POST['fname']
        lName = req.POST['lname']
        userName = req.POST['username']
        email = req.POST['email']
        password1 = req.POST['password1']
        password2 = req.POST['password2']

        myUser = User.objects.create_user(userName,email,password2)
        myUser.first_name = fName
        myUser.last_name = lName
        myUser.save()
        messages.success(req,"Your Account Has Been Created Successfully.")
        return redirect('/logIn/')



    return render(req,'DemoApp/signup.html')

def logIn(req):
    if req.method == 'POST':
        userName = req.POST['username']
        password = req.POST['password']

        user = authenticate(username = userName,password = password)
        
        if user is not None:
            login(req , user)
            detail = Products.objects.all().order_by('?')
            UserName = user.get_username()
            return render(req,'DemoApp/index.html', {'detail': detail , 'username': UserName})
        else:
            messages.error(req,"Email or Password is wrong")
            return redirect('/logIn/')
        
    return render(req,'DemoApp/login.html')

def logOut(req):
    logout(req)
    messages.success(req,"logout successfully")
    return redirect('/')

def profile(req):
    userDetails = req.user
    return render(req,'DemoApp/profile.html',{'userDetails': userDetails})
