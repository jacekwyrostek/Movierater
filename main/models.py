from django.db import models

# Create your models here.
class Movie(models.Model):
    name=models.CharField(max_length=128)
    description=models.TextField(default='')
    year=models.IntegerField(null=True, blank=True)
    imdbRating=models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=4)
    photo=models.ImageField(null=True, blank=True)

    def nameWithYear(self):
        return str(self.name)+' ('+str(self.year)+')'
    def __str__(self):
        return self.nameWithYear()
