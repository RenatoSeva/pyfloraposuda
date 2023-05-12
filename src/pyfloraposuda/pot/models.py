from django.db import models
from django.contrib.auth.models import User

from plant.models import Plant
# Create your models here.

class Pot(models.Model):
    name = models.CharField(max_length=255)
    plant = models.ForeignKey(Plant, related_name='pots', on_delete=models.PROTECT)
    user = models.ForeignKey(User, related_name='pots', on_delete=models.CASCADE)

    def __str__(self):
        return self.name