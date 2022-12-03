from django.urls import path

from restaurant.views import DishesListView, DishTypesListView, CooksListView, CookDetailView, DishDetailView, \
    DishTypeDetailView, index, DishCreateView, DishTypeCreateView, CookCreateView, DishUpdateView, DishTypeUpdateView, \
    CookUpdateView, DishDeleteView, DishTypeDeleteView, CookDeleteView, ExperienceUpdateView

urlpatterns = [
    path("", index, name="home_page"),
    path("dishes/", DishesListView.as_view(), name="dish-list"),
    path("dish_types/", DishTypesListView.as_view(), name="dish-type-list"),
    path("cooks/", CooksListView.as_view(), name="cooks-list"),
    path("cooks/<int:pk>", CookDetailView.as_view(), name="cook-detail"),
    path("cooks/<int:pk>/delete/", CookDeleteView.as_view(), name="cook-delete"),
    path("cooks/<int:pk>/update", CookUpdateView.as_view(), name="cook-update"),
    path("dishes/<int:pk>", DishDetailView.as_view(), name="dish-detail"),
    path("dishes/<int:pk>/delete/", DishDeleteView.as_view(), name="dish-delete"),
    path("dish_types/<int:pk>", DishTypeDetailView.as_view(), name="dish-type-detail"),
    path("dish_types/<int:pk>/update/", DishTypeUpdateView.as_view(), name="dish-type-update"),
    path("dish_types/<int:pk>/delete/", DishTypeDeleteView.as_view(), name="dish-type-delete"),
    path("dishes/create/", DishCreateView.as_view(), name="dish-create"),
    path("dishes/<int:pk>/update/", DishUpdateView.as_view(), name="dish-update"),
    path("dish_types/create/", DishTypeCreateView.as_view(), name="dish-type-create"),
    path("cooks/create/", CookCreateView.as_view(), name="cook-create"),
    path("cooks/<int:pk>/experience_update", ExperienceUpdateView.as_view(), name="experience-update")
]

app_name = "restaurant"
