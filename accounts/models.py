import random
import uuid
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from Base.email import send_account_activation_email
from Base.models import BaseModel
# Create your models here.
class Profile(BaseModel):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    is_email_verified=models.BooleanField(default=False)
    email_token=models.CharField(max_length=100,null=True,blank=True)
    profile_image=models.ImageField(upload_to='profile')




@receiver(post_save, sender=User)
def send_email_token(sender,instance,created,**kwargs):
    try:
        if created:
            email_token = str(uuid.uuid4())           
            Profile.objects.create(user = instance , email_token = email_token)
            email = instance.email
            send_account_activation_email(email,email_token)

    except Exception as e:
        print(e)


class Member(BaseModel):
    member_name= models.CharField(max_length=50)
    member_image=models.ImageField(upload_to='member')
    about_me=models.TextField()

class Donate(BaseModel):
    user=models.ManyToManyField(User,related_name='donate')
    name=models.CharField(max_length=20)
    phone_number=models.IntegerField()
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=20)
    amount=models.IntegerField()
    card_number=models.IntegerField()
    CVV=models.IntegerField()
    pin_code = models.IntegerField(unique=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.pin_code:
            self.pin_code = self.generate_pin_code()
        super().save(*args, **kwargs)

    def generate_pin_code(self):
        # Generate a 6-digit pin code; adjust length as needed
        return random.randint(100000, 999999)

class Volunteer(BaseModel):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    availability = models.CharField(max_length=100, help_text="e.g., Weekends, Weekdays, Flexible")
    skills = models.TextField(help_text="Describe your skills or experience relevant to volunteering.")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
