from multiprocessing import context

from django.shortcuts import render
from django.views.generic import ListView,DetailView
from menu_app.models import Food_category,Food


# Create your views here.


class Food_category_view(ListView):
    model = Food_category
    context_object_name = 'item'
    template_name = "menu_app/category.html"



class Category_detail_view(DetailView):
    model = Food_category
    context_object_name = 'item'
    template_name = "menu_app/category_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Food'] = Food.objects.filter(
            food_category=self.object
        )
        return context



class Food_detail_view(DetailView):
    model = Food
    template_name = 'menu_app/food_detail.html'
    context_object_name = 'i'