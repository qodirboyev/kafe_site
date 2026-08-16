from django.urls import path
from .views import (
    Food_category_view,
    Category_detail_view,
    Food_detail_view,
    food_orders_view,
    increase_food,
    decrease_food,
    remove_food,
    create_order,
)
urlpatterns = [
    path('',Food_category_view.as_view(),name='food_category'),
    path('<int:pk>/category_foods/',Category_detail_view.as_view(),name='category_detail'),
    path('<int:pk>/food/',Food_detail_view.as_view(),name='food_detail'),
    path("food_orders/",food_orders_view,name="food_orders"),
    path("food_orders/increase/<int:food_id>/",increase_food,name="increase_food"),
    path("food_orders/decrease/<int:food_id>/",decrease_food,name="decrease_food"),
    path("food_orders/remove/<int:food_id>/",remove_food, name="remove_food"),
    path(
        "create-order/",
        create_order,
        name="create_order"
    ),
]