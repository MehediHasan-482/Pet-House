from profile import Profile
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Pet, PetDetail
from .forms import AdoptionApplicationForm
from .models import Animal
from .models import AnimalImage
from django.shortcuts import render


# Create your views here.
def get_animal(request,slug):
    try:
        print("Trying to fetch product")
        animal = Animal.objects.get(slug=slug)
        animal_image=AnimalImage.objects.all()
        print("animal found:", animal)
        context = {'animal': animal, 'animal_image': animal_image}

        return render(request, 'aminal/animal.html', context=context)

    except Exception as e:
        print("Error occurred:", e)
        return HttpResponse("An error occurred.", status=500)
    
def animal_detail(request, slug):
    # Fetch the Animal object using the slug
    animal = get_object_or_404(Animal, slug=slug)
    return render(request, 'animal/animal_detail.html', {'animal': animal})
    


# View to list all available pets
def pet_list(request):
    pets = Pet.objects.filter(available=True)
    return render(request, 'animal/pet_list.html', {'pets': pets})

# View for pet details
def pet_detail(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    return render(request, 'animal/pet_detail.html', {'pet': pet})

# View for adopters to apply for a pet
def apply_for_adoption(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    
    if request.method == 'POST':
        form = AdoptionApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.pet = pet
            application.save()
            messages.success(request, 'Your application has been submitted successfully!')
            return redirect('pet_list')
    else:
        form = AdoptionApplicationForm()

    return render(request, 'animal/apply_for_adoption.html', {'form': form, 'pet': pet})





