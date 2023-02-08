from django.shortcuts import render
from django.views import View
from .models import Customer, Product, Cart, OrderPlaced

# def home(request):
#  return render(request, 'app/home.html')

class ProductView(View):
    def get(self, request):
        English = Product.objects.filter(category='E')
        Bengali = Product.objects.filter(category='B')
        Hindi = Product.objects.filter(category='H')
        Old = Product.objects.filter(category='O')
        return render(request, 'app/home.html',
        {'English':English, 'Bengali':Bengali, 'Hindi':Hindi, 'Old':Old})

def product_detail(request):
 return render(request, 'app/productdetail.html')

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request):
 return render(request, 'app/mobile.html')

def login(request):
 return render(request, 'app/login.html')

def customerregistration(request):
 return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')
