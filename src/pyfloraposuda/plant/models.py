from django.db import models

# Create your models here.
class Plant(models.Model):
    """model podataka koji prikazuje pojedinu biljku

    Args:
        models (django base model): model podataka koji prikazuje pojedinu biljku

    Returns:
        str: vraca ime biljke
    """
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='plant_images')
    humidity = models.CharField(max_length=255)
    brightness = models.CharField(max_length=255)
    temperature = models.CharField(max_length=255)
    substrate = models.CharField(max_length=255)

    def __str__(self):
        return self.name
