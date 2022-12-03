from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from restaurant.models import DishType

DISH_TYPE_LIST = reverse("restaurant:dish-type-list")


class PublicDishTypesList(TestCase):
    def test_login_required(self):
        res = self.client.get(DISH_TYPE_LIST)
        self.assertNotEqual(res.status_code, 200)


class PrivateManufacturersList(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create(
            username="user",
            password="user12345",
            years_of_experience=3,
            position="Cook"
        )
        self.client.force_login(self.user)

    def test_retrieve_dish_types(self):
        DishType.objects.create(name="Meat")
        DishType.objects.create(name="Soup")

        dish_types = DishType.objects.all()
        response = self.client.get(DISH_TYPE_LIST)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["dish_types_list"]), list(dish_types))
        self.assertTemplateUsed(response, "restaurant/dish_types_list.html")


class PrivateCookTests(TestCase):

    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="user",
            password="123sssss",
            years_of_experience=3,
            position="Cook"
        )
        self.client.force_login(self.user)

    def test_create_cook(self):
        form_data = {
            "username": "username",
            "password1": "23232lll",
            "password2": "23232lll",
            "first_name": "first_name",
            "last_name": "last_name",
            "position": "Cook",
            "years_of_experience": 3
        }
        self.client.post(reverse("restaurant:cook-create"), data=form_data)
        new_user = get_user_model().objects.get(username=form_data["username"])

        self.assertEqual(new_user.first_name, form_data["first_name"])
        self.assertEqual(new_user.last_name, form_data["last_name"])
        self.assertEqual(new_user.position, form_data["position"])
        self.assertEqual(new_user.years_of_experience, form_data["years_of_experience"])
