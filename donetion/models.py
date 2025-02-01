from django.db import models
import uuid
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

from Base.models import BaseModel

# Create your models here.
class Donetion(BaseModel):
    doner_name=models.CharField(max_length=20,default=True)
    number = models.IntegerField(
        validators=[
            MinValueValidator(10000000000),  # Minimum 11-digit number
            MaxValueValidator(99999999999)  # Maximum 11-digit number
        ]
    )
    transaction_id=models.TextField()
    amount=models.IntegerField()


