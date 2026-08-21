from django.urls import path
from .views import HomeView,Add_comment,Update_comment,Delete_comment


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add_comment/', Add_comment.as_view(), name='add_comment'),
    path('update_comment/<int:pk>/', Update_comment.as_view(), name='update_comment'),
    path('delete_comment/<int:pk>/', Delete_comment.as_view(), name='delete_comment'),
]