from django.db import models

# Create your models here.
class Plant(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='plant_images', blank=True, null=True)
    humidity = models.CharField(max_length=255)
    brightness = models.CharField(max_length=255)
    temperature = models.CharField(max_length=255)
    substrate = models.CharField(max_length=255)

    def __str__(self):
        return self.name
