from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from menu_app.models import Food_category, Food,Order, OrderItem
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class Food_category_view(LoginRequiredMixin,ListView):
    model = Food_category
    context_object_name = 'item'
    template_name = "menu_app/category.html"


class Category_detail_view(LoginRequiredMixin,DetailView):
    model = Food_category
    context_object_name = 'item'
    template_name = "menu_app/category_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['Food'] = Food.objects.filter(
            food_category=self.object
        )

        return context


class Food_detail_view(LoginRequiredMixin,DetailView):
    model = Food
    template_name = 'menu_app/food_detail.html'
    context_object_name = 'i'



@login_required(login_url="login")
def food_orders_view(request):

    if request.method == "POST":

        food_id = request.POST.get("food_id")
        food_soni = int(request.POST.get("food_soni", 1))

        print("FOOD ID:", food_id)
        print("FOOD SONI:", food_soni)

        foods_card = request.session.get("food_card", {})

        foods_card[str(food_id)] = food_soni

        request.session["food_card"] = foods_card
        request.session.modified = True

        print("SESSION:", request.session["food_card"])

    foods_card = request.session.get("food_card", {})

    foods = Food.objects.filter(
        pk__in=foods_card.keys()
    )

    orders = []

    jami_narx = 0

    for food in foods:

        quantity = foods_card[str(food.pk)]

        summa = food.narx * quantity

        jami_narx += summa

        orders.append({
            "food": food,
            "quantity": quantity,
            "summa": summa,
        })

    context = {
        "orders": orders,
        "jami_narx": jami_narx,
    }

    return render(
        request,
        "menu_app/food_orders.html",
        context
    )





@login_required(login_url="login")
def increase_food(request, food_id):

    foods_card = request.session.get("food_card", {})

    food_id = str(food_id)

    if food_id in foods_card:
        foods_card[food_id] += 1

    request.session["food_card"] = foods_card
    request.session.modified = True

    return redirect("food_orders")



@login_required(login_url="login")
def decrease_food(request, food_id):

    foods_card = request.session.get("food_card", {})

    food_id = str(food_id)

    if food_id in foods_card:

        foods_card[food_id] -= 1

        if foods_card[food_id] <= 0:
            del foods_card[food_id]

    request.session["food_card"] = foods_card
    request.session.modified = True

    return redirect("food_orders")


@login_required(login_url="login")
def remove_food(request, food_id):

    foods_card = request.session.get("food_card", {})

    food_id = str(food_id)

    if food_id in foods_card:
        del foods_card[food_id]

    request.session["food_card"] = foods_card
    request.session.modified = True

    return redirect("food_orders")


@login_required(login_url="login")
def create_order(request):

    foods_card = request.session.get("food_card", {})

    if not foods_card:
        return redirect("food_orders")

    order = Order.objects.create()

    for food_id, quantity in foods_card.items():

        food = Food.objects.get(pk=food_id)

        OrderItem.objects.create(
            order=order,
            food=food,
            quantity=quantity,
            price=food.narx
        )

    del request.session["food_card"]

    return redirect("order_success")