from django.shortcuts import redirect, render
from .forms import UserForm
from django.contrib import messages
from .models import User,Buyer,Seller
from django.contrib.auth.models import auth

# Create your views here.
def buy_register(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2 and len(password1)>7 :
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken.')
                return redirect('buy_register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already taken.')
                return redirect('buy_register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, is_buyer=True)
                user.save()
                request.session['username'] = username
                return redirect('buy_info')
        else:
            messages.info(request, 'Password not matching.')
            return redirect('buy_register')
    else:
        return render(request, 'buy_register.html')


def sell_register(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2 and len(password1)>7 :
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken.')
                return redirect('sell_register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already taken.')
                return redirect('sell_register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, is_seller=True)
                user.save()
                request.session['username'] = username
                return redirect('sell_info')
        else:
            messages.info(request, 'Password not matching.')
            return redirect('sell_register')
    else:
        return render(request, 'sell_register.html')



def buy_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None and user.is_buyer:
            auth.login(request, user)
            return redirect('/buy/buyProduct')
        else:
            messages.info(request, 'invalid credentials.')
            return redirect('buy_login')

    else:
        return render(request, 'buy_login.html')    
    

def sell_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None and user.is_seller:
            auth.login(request, user)

            return redirect('/sell/orders')
        else:
            messages.info(request, 'invalid credentials.')
            return redirect('sell_login')

    else:
        return render(request, 'sell_login.html')    

def sell_info(request):
    if request.method == 'POST':
        name = request.POST['name']
        company = request.POST['company']
        gstin = request.POST['gstin']
        phone = request.POST['phone']
        
        if len(gstin) == 15:
            if len(phone) == 10:

                username = request.session['username']
                user_name = User.objects.filter(username=username)[0]
                
                seller = Seller.objects.create(user=user_name, name=name, company=company, gstin=gstin, phone=phone)
                seller.save()
                return redirect('sell_login')
            
            else:
                messages.info(request, 'Phone number is 10 digits')
                return redirect('sell_info')


        else:
            messages.info(request, 'GST number length is 15')
            return redirect('sell_info')

    else:
        return render(request, 'sell_info.html')    

    


def buy_info(request):
    if request.method == 'POST':
        name = request.POST['name']
        company = request.POST['company']
        gstin = request.POST['gstin']
        phone = request.POST['phone']
        
        if len(gstin) == 15:
            if len(phone) == 10:

                username = request.session['username']
                user_name = User.objects.filter(username=username)[0]
                buyer = Buyer.objects.create(user=user_name, name=name, company=company, gstin=gstin, phone=phone )
                buyer.save()
                return redirect('buy_login')
            
            else:
                messages.info(request, 'Phone number is 10 digits')
                return redirect('buy_info')


        else:
            messages.info(request, 'GST number length is 15')
            return redirect('buy_info')

    else:
        return render(request, 'buy_info.html')    

