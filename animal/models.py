from django.db import models

# Create your models here.
import uuid
from django.db import models
from Base.models import BaseModel
from django.utils.text import slugify
from django.contrib.auth.models import User



class Category(BaseModel):
    # category=models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    category_image = models.ImageField(upload_to="categories")

    def save(self, *args, **kwargs):
        self.slug=slugify(self.category_name)
        super(Category,self).save(*args, **kwargs)

    def __str__(self):
        return self.category_name


class Animal(BaseModel):
    # product=models.AutoField(primary_key=True)
    animal_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="animals")
    gender=models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    weight = models.IntegerField()
    colour = models.CharField(max_length=100)
    animal_description = models.TextField()


    def save(self, *args, **kwargs):
        self.slug=slugify(self.animal_name)
        super(Animal,self).save(*args, **kwargs)

    def __str__(self)->str:
        return self.animal_name
    
class AnimalDetail(models.Model):
    animal = models.OneToOneField(Animal, on_delete=models.CASCADE, related_name='details')
    health_status = models.CharField(max_length=100, help_text=("General health condition of the pet"))
    vaccination_status = models.TextField(help_text=("Details of completed vaccinations"))
    microchipped = models.BooleanField(default=False, help_text=("Indicates if the pet is microchipped"))
    spayed_neutered = models.BooleanField(default=False, help_text=("Indicates if the pet is spayed or neutered"))
    special_needs = models.TextField(null=True, blank=True, help_text=("Details of any special care requirements"))

    def __str__(self):
        return f"Details for {self.animal.animal_name}"

class AnimalImage(BaseModel):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name="animal_images")
    image = models.ImageField(upload_to="animal")


    
    def save(self, *args, **kwargs):
        self.slug=slugify(self.animal_name)
        super(Animal,self).save(*args, **kwargs)

    # def __str__(self)->str:
    #     return self.animal_name


class Pet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()  # Age in years
    breed = models.CharField(max_length=100, blank=True, null=True)
    species = models.CharField(max_length=50, choices=[('dog', 'Dog'), ('cat', 'Cat'), ('other', 'Other')])
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')])
    description = models.TextField(blank=True, null=True)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='pet_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class PetDetail(models.Model):
    pet = models.OneToOneField(Pet, on_delete=models.CASCADE, related_name='pet_details')
    health_status = models.CharField(max_length=100, help_text=("General health condition of the pet"))
    vaccination_status = models.TextField(help_text=("Details of completed vaccinations"))
    microchipped = models.BooleanField(default=False, help_text=("Indicates if the pet is microchipped"))
    spayed_neutered = models.BooleanField(default=False, help_text=("Indicates if the pet is spayed or neutered"))
    special_needs = models.TextField(null=True, blank=True, help_text=("Details of any special care requirements"))

    def __str__(self):
        return f"Details for {self.pet.name}"
    

class Adopter(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Medicine(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    dosage = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=255)
    image = models.ImageField(upload_to='medicines', null=True, blank=True)
    stock_quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
class Doctor(models.Model):
    name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=255)
    image = models.ImageField(upload_to='doctors/', null=True, blank=True)

    def __str__(self):
        return self.name



class AdoptionApplication(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='applications')
    adopter = models.ForeignKey(Adopter, on_delete=models.CASCADE, related_name='applications')
    application_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Application by {self.adopter} for {self.pet}"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    medicine = models.ForeignKey('Medicine', on_delete=models.CASCADE, related_name="orders")
    quantity = models.PositiveIntegerField(default=1)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.medicine.name} - {self.quantity}"