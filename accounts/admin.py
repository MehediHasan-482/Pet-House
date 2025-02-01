from django.contrib import admin
from animal.models import Adopter, Order
from .models import Profile, Volunteer

# Register your models here.
admin.site.register(Profile)
@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'availability', 'created_at')
    search_fields = ('first_name', 'last_name', 'email', 'phone_number')
    list_filter = ('availability', 'created_at')
    ordering = ('created_at',)


@admin.register(Adopter)
class AdopterAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'address', 'created_at')  # Include any new fields you want to display
    search_fields = ('first_name', 'last_name', 'email', 'phone_number')  # You can add more fields for search
    list_filter = ('created_at',)  # Optionally, filter by creation date if needed
    ordering = ('-created_at',)  # Order adopters by creation date (latest first)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'medicine', 'quantity', 'purchase_date')  # Fields to display
    list_filter = ('purchase_date',)  # Filter options
    search_fields = ('user__username', 'medicine__name')  # Searchable fields
    ordering = ('-purchase_date',)  # Default ordering
