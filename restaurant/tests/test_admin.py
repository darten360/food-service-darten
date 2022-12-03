from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class AdminSiteTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="admin12345",
            position="Chief",
            years_of_experience=10
        )
        self.client.force_login(self.admin_user)
        self.cook = get_user_model().objects.create_user(
            username="driver",
            password="12345driver",
            position="Co-Chief",
            years_of_experience=5
        )

    def test_position_listed(self):
        url = reverse("admin:restaurant_cook_changelist")
        res = self.client.get(url)

        self.assertContains(res, self.cook.position)

    def test_experience_listed(self):
        url = reverse("admin:restaurant_cook_changelist")
        res = self.client.get(url)

        self.assertContains(res, self.cook.years_of_experience)

    def test_cook_detailed_position_listed(self):
        url = reverse("admin:restaurant_cook_change", args=[self.cook.pk])
        res = self.client.get(url)

        self.assertContains(res, self.cook.position)

    def test_cook_detailed_experience_listed(self):
        url = reverse("admin:restaurant_cook_change", args=[self.cook.pk])
        res = self.client.get(url)

        self.assertContains(res, self.cook.years_of_experience)
