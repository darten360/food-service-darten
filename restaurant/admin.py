from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from restaurant.models import Dish, DishType, Cook


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "price", "dish_type"]
    list_filter = ["dish_type", "price"]
    search_fields = ["name", "description"]


@admin.register(DishType)
class DishTypeAdmin(admin.ModelAdmin):
    search_fields = ["name"]


@admin.register(Cook)
class CookAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("position", "years_of_experience")
    fieldsets = UserAdmin.fieldsets + (("Additional info", {"fields": ("position", "years_of_experience")}), )
    add_fieldsets = UserAdmin.add_fieldsets + (("Additional info", {"fields": (
        "first_name",
        "last_name",
        "position",
        "years_of_experience"
    )}), )

