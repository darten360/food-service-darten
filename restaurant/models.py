from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class DishType(models.Model):
    name = models.CharField(max_length=50, null=False)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"


class Cook(AbstractUser):
    position = models.CharField(max_length=30, default="Cook")
    years_of_experience = models.IntegerField()

    class Meta:
        ordering = ["username"]

    def __str__(self):
        return f"{self.username}, {self.first_name} {self.last_name}"


class Dish(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False)
    description = models.TextField(null=False)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    dish_type = models.ForeignKey(DishType,
                                  on_delete=models.CASCADE,
                                  related_name="dishes")
    cooks = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="dishes")

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Dishes"

    def __str__(self):
        return f"{self.name}"
