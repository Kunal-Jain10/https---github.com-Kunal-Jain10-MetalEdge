from typing import Protocol
from django.http.response import Http404
from django.shortcuts import render
from Account.models import User,Seller,Buyer
from Sell.models import Product
from Buy.models import Order
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
def buyProduct(request):
    
    products = Product.objects.all()

    context = {
        'products':products
    }

    return render(request,'buyProduct.html', context )

def buyOrder(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        quantity = request.POST['quantity']
        
        order = Order.objects.create(seller=product.seller, buyer=request.user.buyer, product=product, quantity=quantity)    
        order.save()
        messages.info(request, 'Product order placed')
        
    context = {
        'product':product
    }

    return render(request, 'buyOrder.html', context)

def buy_orders(request):

    orders = Order.objects.filter(buyer=request.user.buyer)

    context = {
        'orders':orders
    }

    return render(request, 'buy_orders.html', context)


def download(request,path):
    file_path=os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path,'rb')as fh:
            response=HttpResponse(fh.read(),content_type="application/")
            response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
            return response
    
    raise Http404