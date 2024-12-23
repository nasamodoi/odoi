from rest_framework import generics
from .models import TourCategory, Tour, Booking
from .serializers import TourCategorySerializer, TourSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticated


class TourListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Tour.objects.all()
    serializer_class = TourSerializer

# List and Create Tour Categories
class TourCategoryListCreateView(generics.ListCreateAPIView):
    queryset = TourCategory.objects.all()
    serializer_class = TourCategorySerializer

# Retrieve, Update, and Delete a Single Tour Category
class TourCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TourCategory.objects.all()
    serializer_class = TourCategorySerializer

# List and Create Tours
class TourListCreateView(generics.ListCreateAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer

# Retrieve, Update, and Delete a Single Tour
class TourDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer

# List and Create Bookings
class BookingListCreateView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

# Retrieve, Update, and Delete a Single Booking
class BookingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
