from django.urls import path
from animal.views import animal_detail, apply_for_adoption, get_animal,pet_detail, pet_list
from django.urls import path

urlpatterns = [
    path('petlist/', pet_list, name='pet_list'),
    path('<slug:slug>/', get_animal, name='get_animal'),
    path('pet/<uuid:pet_id>/', pet_detail, name='pet_detail'),
    path('adopt/<uuid:pet_id>/', apply_for_adoption, name='apply_for_adoption'),
    path('animal/<slug:slug>/', animal_detail, name='animal_detail'),
    
    
]