from django.shortcuts import render
from animal.models import Animal
from django.http import HttpResponseRedirect
from django.http import HttpResponse

# Create your views here.

def index(request):

    print("hello")
    context = {'animals' : Animal.objects.all()}
    print("hello")
    print("mehedi")
    return render(request,'home/index.html',context)
