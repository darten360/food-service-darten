from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic

from restaurant.forms import CookForm, CookCreationForm, CookUpdateForm, DishForm, DishSearchForm
from restaurant.models import Dish, DishType, Cook


@login_required
def index(request):
    """View function for the home page of the site."""

    num_dishes = Dish.objects.count()
    num_cooks = Cook.objects.count()
    num_dish_types = DishType.objects.count()
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_dishes": num_dishes,
        "num_cooks": num_cooks,
        "num_dish_types": num_dish_types,
        "num_visits": num_visits + 1
    }

    return render(request, "restaurant/index.html", context=context)


class DishesListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    template_name = "restaurant/dishes_list.html"
    context_object_name = "dishes"
    queryset = Dish.objects.all().select_related("dish_type")
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DishesListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")

        context["search_form"] = DishSearchForm(initial={
            "name": name
        })

        return context

    def get_queryset(self):
        form = DishSearchForm(self.request.GET)

        if form.is_valid():
            return self.queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )

        return self.queryset


class DishTypesListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    template_name = "restaurant/dish_types_list.html"
    context_object_name = "dish_types_list"
    paginate_by = 3


class CooksListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    template_name = "restaurant/cooks_list.html"
    context_object_name = "cooks_list"
    paginate_by = 3


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook
    template_name = "restaurant/cook_detail.html"


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish
    template_name = "restaurant/dish_detail.html"


class DishTypeDetailView(LoginRequiredMixin, generic.DetailView):
    model = DishType
    template_name = "restaurant/dish_type_detail.html"
    context_object_name = "dish_type_detail"


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    form_class = DishForm

    def get_success_url(self):
        return reverse('restaurant:dish-detail', kwargs={'pk': self.object.pk})


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    fields = "__all__"
    template_name = "restaurant/dish-type-form.html"

    def get_success_url(self):
        return reverse('restaurant:dish-type-detail', kwargs={'pk': self.object.pk})


class CookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Cook
    form_class = CookCreationForm

    def get_success_url(self):
        return reverse('restaurant:cook-detail', kwargs={'pk': self.object.pk})


class CookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cook
    form_class = CookUpdateForm

    def get_success_url(self):
        return reverse('restaurant:cook-detail', kwargs={'pk': self.object.pk})


class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    fields = "__all__"
    template_name = "restaurant/dish-type-form.html"

    def get_success_url(self):
        return reverse('restaurant:dish-type-detail', kwargs={'pk': self.object.pk})


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    form_class = DishForm

    def get_success_url(self):
        return reverse('restaurant:dish-detail', kwargs={'pk': self.object.pk})


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    template_name = "restaurant/dish_delete_form.html"
    success_url = reverse_lazy("restaurant:dish-list")


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    template_name = "restaurant/dish_type_delete_form.html"
    success_url = reverse_lazy("restaurant:dish-type-list")


class CookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cook
    template_name = "restaurant/cook_delete_form.html"
    success_url = reverse_lazy("restaurant:cooks-list")


class ExperienceUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cook
    form_class = CookForm
    template_name = "restaurant/experience_form.html"

    def get_success_url(self):
        return reverse('restaurant:cook-detail', kwargs={'pk': self.object.pk})
