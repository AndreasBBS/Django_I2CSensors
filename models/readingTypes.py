from .models import Reading
from django.db import models

class Temperature(Reading):
    CELCIUS = 'C'
    FAHRENHEIT = 'F'
    KELVIN = 'K'
    UNIT_CHOICES = (
        (CELCIUS, 'Celcius'),
        (FAHRENHEIT, 'Fahrenheit'),
        (KELVIN, 'Kelvin'),
    )

    unit = models.CharField(
        max_length = 2,
        choices = UNIT_CHOICES,
    )

    unitMeasurement = models.IntegerField(
        editable = False
    )

    # OVERRIDE
    def __str__(self):
        return 'Temperature: ' + self.unitMeasurement + ' ' + self.unit

    # OVERRIDE
    def getAttributesDictionary(self):
        return super.getAttributesDictionary().update({
            self.__class__.__name__ : (self.unit, self.unitMeasurement)    
            })
