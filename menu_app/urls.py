from django.urls import path
from .views import Food_category_view,Category_detail_view,Food_detail_view

urlpatterns = [
    path('',Food_category_view.as_view(),name='food_category'),
    path('<int:pk>/category_foods/',Category_detail_view.as_view(),name='category_detail'),
    path('<int:pk>/food/',Food_detail_view.as_view(),name='food_detail'),
]