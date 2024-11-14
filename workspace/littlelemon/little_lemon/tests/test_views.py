from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from little_lemon.models import Menu
from little_lemon.serializers import MenuSerializer

class MenuViewTest(TestCase):
    
    def setUp(self):
        menu1 = Menu.objects.create(title="Pizza", price=8.99,inventory=50)
        menu2 = Menu.objects.create(title="Burger", price=5.99,inventory=22)
        menu3 = Menu.objects.create(title="Pasta", price=7.99,inventory=33)

    def test_getall(self):
        # Get response from the API view
        response = self.client.get(reverse('menu'))  
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)

        # Assert that response status is 200 OK
        self.assertEqual(response.status_code, 200)

        # Assert that serialized data matches response data
        self.assertEqual(response.data, serializer.data)
