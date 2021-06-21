from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Car

# Create your tests here.

class CarModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(
            username='tester',
            password='pass'
        )
        test_user.save()

        test_car = Car.objects.create(
            name = 'lancer',
            maker = 'mitsubishi',
            year = 2020,
            admin = test_user,
        )
        test_car.save()

    def test_car_content(self):
        car = Car.objects.get(id=1)
        self.assertEqual(car.name, 'lancer')
        self.assertEqual(car.maker, 'mitsubishi')
        self.assertEqual(car.year, 2020)
        self.assertEqual(str(car.admin), 'tester')