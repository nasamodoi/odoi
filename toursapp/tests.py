from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase
from rest_framework import status
from .models import TourCategory

class TourCategoryAPITest(APITestCase):
    def test_create_category(self):
        data = {"name": "Adventure", "description": "Adventure tours"}
        response = self.client.post('/api/categories/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
