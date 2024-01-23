from django.db import models
from musician.models import Musician

# Create your models here.


class Album(models.Model):
    name = models.CharField(max_length=50)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    release_date = models.DateField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)

    def __str__(self):
        return self.name + " - " + self.musician.first_name + " " + self.musician.last_name
