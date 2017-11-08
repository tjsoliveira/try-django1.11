from django.db import models

# Create your models here.
class RestaurantLocation(models.Model):

    name        = models.CharField(max_length=120)
    location    = models.CharField(blank=True, null=True, max_length=120)
