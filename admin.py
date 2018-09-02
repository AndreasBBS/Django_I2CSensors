from django.contrib import admin

from Django_I2CSensors.models.models import Command, I2CSensor

admin.site.register(I2CSensor)
admin.site.register(Command)