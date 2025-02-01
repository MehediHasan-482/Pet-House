from django.contrib import admin
from .models import Animal, AnimalDetail,AnimalImage,Category,Pet, AdoptionApplication, PetDetail

# Register your models here.
class AnimalImageAdmin(admin.StackedInline):
    model=AnimalImage

class AnimalAdmin(admin.ModelAdmin):
    inlines=[AnimalImageAdmin]


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'species', 'breed', 'available', 'created_at')
    list_filter = ('species', 'available')
    search_fields = ('name', 'breed')


@admin.register(AdoptionApplication)
class AdoptionApplicationAdmin(admin.ModelAdmin):
    list_display = ('pet', 'adopter', 'status', 'application_date')
    list_filter = ('status',)
    search_fields = ('adopter__first_name', 'pet__name')

class AnimalDetailInline(admin.StackedInline):
    model = AnimalDetail
    can_delete = False
    verbose_name_plural = 'Animal Details'

# # # Admin configuration for Animal
# @admin.register(Animal)
# class AnimalAdmin(admin.ModelAdmin):
#     list_display = ('animal_name', 'category', 'gender', 'age', 'weight', 'colour')
#     search_fields = ('animal_name', 'category__name', 'gender')
#     list_filter = ('category', 'gender')
#     inlines = [AnimalDetailInline]

# # Register AnimalDetail as standalone (optional if you want direct access to AnimalDetail)
@admin.register(AnimalDetail)
class AnimalDetailAdmin(admin.ModelAdmin):
    list_display = ('animal', 'health_status', 'vaccination_status', 'microchipped', 'spayed_neutered')
    search_fields = ('animal__animal_name', 'health_status')
    list_filter = ('microchipped', 'spayed_neutered')

@admin.register(PetDetail)
class PetDetailAdmin(admin.ModelAdmin):
    list_display = ('pet', 'health_status', 'vaccination_status', 'microchipped', 'spayed_neutered')
    search_fields = ('pet__name', 'health_status')
    list_filter = ('microchipped', 'spayed_neutered')

admin.site.register(Animal, AnimalAdmin)
admin.site.register(Category)
admin.site.register(AnimalImage)
# admin.site.register(AnimalDetail)
from .models import Medicine

admin.site.register(Medicine)
