from django.db import models

# Create your models here.
class TourCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='categories/images/', blank=True, null=True)  # Added image field

    class Meta:
        app_label = 'toursapp'

    def __str__(self):
        return self.name


class Tour(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(TourCategory, on_delete=models.CASCADE, related_name="tours")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_spots = models.PositiveIntegerField(default=0)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='tours/images/',  blank=True, null=True)  # Added image field

    def __str__(self):
        return self.name


class Booking(models.Model):
    tours = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name="bookings")
    customer_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    booking_date = models.DateTimeField(auto_now_add=True)
    number_of_people = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.total_price = self.number_of_people * self.tours.price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.customer_name} - {self.tours.name}"
