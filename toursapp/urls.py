from django.urls import path
from toursapp import views
from .auth_views import LoginView, LogoutView
from .auth_views import RegisterUserView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
       # Token endpoints
       path('register/', RegisterUserView.as_view(), name='user-register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
     path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),



    path('categories/', views.TourCategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', views.TourCategoryDetailView.as_view(), name='category-detail'),
    path('tours/', views.TourListCreateView.as_view(), name='tour-list-create'),
    path('tours/<int:pk>/', views.TourDetailView.as_view(), name='tour-detail'),
    path('bookings/', views.BookingListCreateView.as_view(), name='booking-list-create'),
    path('bookings/<int:pk>/', views.BookingDetailView.as_view(), name='booking-detail'),
]
