from django.test import TestCase
from little_lemon.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        item=Menu.objects.create(title="ice cream", price=8, inventory=50)
        self.assertEqual(item,"ice cream:8")