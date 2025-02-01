from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from accounts.models import send_email_token
from Base.email import send_account_activation_email 
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from animal.models import Medicine, Order
from .models import Profile
from array import *
from django.http import HttpResponseRedirect
# Create your views here.

@csrf_exempt
def login_page(request):
        
    if request.method == 'POST':   
        email=request.POST.get('email')
        password=request.POST.get('password')
        user_obj = User.objects.filter(username=email)
        print('hello1')

        if not user_obj.exists():
            messages.warning(request, "Account not found.")
            print('hello2')
            return HttpResponseRedirect(request.path_info)    

        if not user_obj[0].profile.is_email_verified:
            messages.warning(request, "your account is not verified.")
            print('hello3')
            return HttpResponseRedirect(request.path_info)

        user_obj = authenticate(username=email, password=password)
        if user_obj:
            # print('email',email)
            # print('password',password)
            # messages.success(request, "Your account has been created successfully.")
            login(request, user_obj)
            messages.success(request, "An email has been sent on your mail.")
            # return render(request,'home/index.html')
            return redirect('/')

        messages.warning(request, "Invalid credential.")
        return HttpResponseRedirect(request.path_info)


    return render(request, 'accounts/login.html')

def logout(request):
    auth_logout(request)
    return redirect('/')

@csrf_exempt
def register_page(request):

    if request.method == 'POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        user_obj = User.objects.filter(username=email)

        if user_obj.exists():
            messages.warning(request, "Email is already taken.")
            return HttpResponseRedirect(request.path_info)    
        
        print(email)

        user_obj = User.objects.create(first_name=first_name,last_name=last_name,email=email,username=email)
        user_obj.set_password(password)
        user_obj.save()

        messages.success(request, "An email has been sent on your mail.")
        # send_account_activation_email(email)
        # send_mail(subject, message, email_from, recipient_list)
        return HttpResponseRedirect(request.path_info)
    
    return render(request, 'accounts/register.html')



def activate_email(request,email_token):
    try:
        user = Profile.objects.get(email_token=email_token)
        user.is_email_verified=True
        user.save()
        return redirect('/')
    except Exception as e:
        return HttpResponse('Invalied Email Token')


def adopt_or_get_involved(request):
    return render(request, 'accounts/adopt.html')


from django.shortcuts import render, redirect
from .forms import AdopterForm, VolunteerForm

def volunteer_register(request):
    if request.method == 'POST':
        form = VolunteerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration Successful!! Thank you for registering as an volenteer.")
            return HttpResponseRedirect(request.path_info)
    else:
        form = VolunteerForm()
    return render(request, 'accounts/volunteer_register.html', {'form': form})

# def volunteer_success(request):
#     return render(request, 'volunteer_success.html')


def adopter_register(request):
    if request.method == 'POST':
        form = AdopterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration Successful!! Thank you for registering as an adopter.")
            return HttpResponseRedirect(request.path_info)
    else:
        form = AdopterForm()
    return render(request, 'accounts/adopter_register.html', {'form': form})

def medicine_list(request):
    medicines = Medicine.objects.all()
    return render(request, 'accounts/medicine_list.html', {'medicines': medicines})

def buy_medicine(request, medicine_id):
    medicine = get_object_or_404(Medicine, id=medicine_id)
    if medicine.stock_quantity > 0:
        # Logic to handle purchase (e.g., reduce stock quantity, process payment)
        Order.objects.create(user=request.user, medicine=medicine, quantity=1)
        medicine.stock_quantity -= 1
        medicine.save()
        # Redirect to a success page or confirmation
        return redirect('purchase_success')
    else:
        # Redirect to an error page or message
        return redirect('out_of_stock')
    


def purchase_success(request):
    return render(request, 'accounts/purchase_success.html', {})

def out_of_stock(request):
    return render(request, 'accounts/out_of_stock.html', {})

@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user).order_by('-purchase_date')
    return render(request, 'accounts/order_list.html', {'orders': orders})