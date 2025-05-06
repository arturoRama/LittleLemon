from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        # Create test Menu instances
        self.menu1 = Menu.objects.create(title="Burger", price=9.99, inventory=20)
        self.menu2 = Menu.objects.create(title="Pizza", price=15.50, inventory=10)
        self.menu3 = Menu.objects.create(title="Salad", price=6.75, inventory=30)
        self.client = APIClient()

    def test_getall(self):
        # Get response from the API
        response = self.client.get('http://127.0.0.1:8000/restaurant/menu/')

        # Serialize data
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)

        # Assertions
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)