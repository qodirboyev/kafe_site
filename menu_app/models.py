from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
# Create your models here.

class Food_category(models.Model):
    image = models.ImageField(upload_to='food_category/')
    name = models.CharField(max_length=100)
    info = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', args=[self.pk])


class Food(models.Model):
    image = models.ImageField(upload_to='foods_image/')
    name = models.CharField(max_length=100)
    info = models.TextField(null=True, blank=True)
    narx = models.FloatField()
    food_category = models.ForeignKey(Food_category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('food_detail', args=[self.pk])





class Order(models.Model):

    STATUS_CHOICES = [
        ("new", "Yangi"),
        ("accepted", "Qabul qilindi"),
        ("cooking", "Tayyorlanmoqda"),
        ("ready", "Tayyor"),
        ("completed", "Yakunlandi"),
        ("cancelled", "Bekor qilindi"),
    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="new"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Buyurtma #{self.pk}"

class OrderItem(models.Model):

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="items"
    )

    food = models.ForeignKey(
        Food,
        on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField()

    price = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.food.name} x {self.quantity}"