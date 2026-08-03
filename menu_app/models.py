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