from django.contrib import admin
from .models import Pot, Senzors, SenzorValues

# Register your models here.
admin.site.register(Pot)
admin.site.register(Senzors)
admin.site.register(SenzorValues)
