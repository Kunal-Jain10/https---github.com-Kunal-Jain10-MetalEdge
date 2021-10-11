from django.shortcuts import render

from Account.models import Seller,Buyer,User
from Buy.models import Order
from .forms import ProductForm
from .models import Product


# Create your views here.
def orders(request):

    orders = Order.objects.filter(seller=request.user.seller)
    context = {
        'orders':orders
    }
    return render(request,'orders.html', context)

def addProduct(request):
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            instance=form.save(commit=False)        
            instance.seller = request.user.seller
            instance.save()        
    
    context={'form':form}
    return render(request,'addProduct.html', context)

def viewProduct(request):
    
    products = request.user.seller.products.all()

    context = {
        'products':products
    }

    return render(request,'viewProduct.html', context )

def productDetail(request,pk):
    
    product = Product.objects.get(pk=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES, instance=product)
        if form.is_valid():
            form.save()    

    context = {
        'form':form,
        'product':product
    }
    
    return render(request,'productDetail.html', context )

