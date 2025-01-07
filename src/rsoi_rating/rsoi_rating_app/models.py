from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Rating(models.Model):
    username = models.CharField(max_length=80)
    stars = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])