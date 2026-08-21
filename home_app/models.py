from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator
from django.urls import reverse
from django.db import models

# Create your models here.
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    star = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('home')