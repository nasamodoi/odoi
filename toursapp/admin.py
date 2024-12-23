from django.contrib import admin

# Register your models here.
from .models import TourCategory, Tour, Booking

admin.site.register(TourCategory)  
admin.site.register(Tour)
admin.site.register(Booking)