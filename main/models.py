from django.db import models

# Create your models here.
class Movie(models.Model):
    name=models.CharField(max_length=128)
    description=models.TextField(default='')
    year=models.IntegerField(null=True, blank=True)
    released=models.DateField(null=True, blank=True)
    imdRating=models.DecimalField(null=True, blank=True, decimal_places=7, max_digits=10)
    photo=models.ImageField(null=True, blank=True)
