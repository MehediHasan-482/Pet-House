from django import forms

from animal.models import Adopter
from .models import Volunteer

class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address', 'availability', 'skills']


class AdopterForm(forms.ModelForm):
    class Meta:
        model = Adopter
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address']
