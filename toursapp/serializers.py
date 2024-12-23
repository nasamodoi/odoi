from rest_framework import serializers
from .models import TourCategory, Tour, Booking


class TourCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TourCategory
        fields = ['id', 'name', 'description','image']

class TourSerializer(serializers.ModelSerializer):
    category = TourCategorySerializer(read_only=True)  # Nested serializer for read
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=TourCategory.objects.all(),  # Foreign key for write
        source='category',
        write_only=True
    )

    class Meta:
        model = Tour
        fields = [
            'id', 'name', 'description', 'category', 'category_id',
            'price', 'image','available_spots', 'start_date', 'end_date', 'is_active'
        ]



class BookingSerializer(serializers.ModelSerializer):
    tours = TourSerializer(read_only=True)
    tours_id = serializers.PrimaryKeyRelatedField(
        queryset=Tour.objects.all(),
        source='tours',
        write_only=True
    )

    class Meta:
        model = Booking
        fields = [
            'id', 'tours', 'tours_id', 'customer_name', 
            'email', 'phone_number', 'booking_date', 
            'number_of_people', 'total_price'
        ]
        read_only_fields = ['total_price', 'booking_date']
