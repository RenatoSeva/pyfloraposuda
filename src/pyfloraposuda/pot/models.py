from django.db import models
from django.contrib.auth.models import User

from plant.models import Plant
# Create your models here.


class Senzors(models.Model):
    type = models.CharField(max_length=255)
    currentValue = models.FloatField(default=0)
    date = models.DateTimeField(auto_now_add=True)

class SenzorValues(models.Model):
    senzor = models.ForeignKey(Senzors, related_name='senzors', on_delete=models.PROTECT)
    value = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)



class Pot(models.Model):
    name = models.CharField(max_length=255)
    plant = models.ForeignKey(Plant, related_name='potsPlant', on_delete=models.PROTECT, null=True, blank=True)
    user = models.ForeignKey(User, related_name='potsUser', on_delete=models.CASCADE)
    senzorTmp = models.ForeignKey(Senzors, related_name='potsSenzorTmp', on_delete=models.PROTECT)
    senzorPh = models.ForeignKey(Senzors, related_name='potsSenzorPh', on_delete=models.PROTECT)
    senzorBrightness = models.ForeignKey(Senzors, related_name='potsSenzorBrightness', on_delete=models.PROTECT)
    senzorHumidity = models.ForeignKey(Senzors, related_name='potsSenzorHumidity', on_delete=models.PROTECT)
    status = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name