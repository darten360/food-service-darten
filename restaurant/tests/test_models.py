from django.contrib.auth import get_user_model
from django.test import TestCase

from restaurant.models import Dish, DishType, Cook


class ModelsTests(TestCase):
    def test_driver_str(self):
        cook = get_user_model().objects.create_user(
            username="danchik",
            password="1231244fff",
            years_of_experience=3,
            first_name="Danylo",
            last_name="Kriuchock"
        )

        self.assertEqual(str(cook), f"{cook.username}, {cook.first_name} {cook.last_name}")

    def test_dish_str(self):
        dish_type = DishType.objects.create(name="Desserts")
        dish = Dish.objects.create(
            name="Ice Cream",
            description="Frozen milk with cream and fruits or something else",
            price=123,
            dish_type_id=dish_type.id,
        )

        self.assertEqual(str(dish), f"{dish.name}")

    def test_dish_type_str(self):
        dish_type = DishType.objects.create(name="Desserts")

        self.assertEqual(str(dish_type), f"{dish_type.name}")

    def test_cook_with_exp_and_pos_str(self):
        username = "test username"
        password = "test password"
        years_of_experience = 3
        position = "Chief"
        cook = get_user_model().objects.create_user(
            username=username,
            password=password,
            years_of_experience=years_of_experience,
            position=position
        )

        self.assertEqual(cook.username, username)
        self.assertTrue(cook.check_password(password))
        self.assertEqual(cook.years_of_experience, years_of_experience)
        self.assertEqual(cook.position, position)
