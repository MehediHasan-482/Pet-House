from django.contrib import messages
from django.shortcuts import render
from .models import Donetion

# Create your views here.

def get_donetion(request):
    if request.method == 'POST':
        doner_name=request.POST.get('cardholder_name')
        number=request.POST.get('card_number')
        transaction_id=request.POST.get('trans_number')
        amount=request.POST.get('amount')    

        donation_obj = Donetion.objects.create(doner_name=doner_name,number=number,transaction_id=transaction_id,amount=amount)
        donation_obj.save()
        messages.success(request, "Donation successfull.")

    return render(request, 'donetion/donetion.html')

