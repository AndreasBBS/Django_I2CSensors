from django.db import models

class I2CSensor(models.Model):
    # latestReading = models.ForeignKey(Reading, on_delete=models.CASCADE)
    # commands = 
    # bus = 
    # connected = models.Boolean(isBusConnected())
    # historyReadings = models.Foreignkey(ReadingCointainer, on_delete=models.CASCADE)
    # type = models.CharField(max_length = 30)
    # name = models.CharField(max_length = 126)
    # (optional fields)
    # shortDescription = models.CharField(max_length = 254) 
    # reference = models.CharField(max_length = 30)
    address = models.CharField(
        max_length = 4
    )

    ## functions

    # OVERRIDE
    def __str__(self):
        return self.address

class Reading(models.Model):
    timeStamp = models.DateTimeField(
        default = models.datetime.datetime.now,
        editable = False
    )

    rawMeasurement = models.IntegerField(
        editable = False
    )

    def accept(self, visitor):
        visitor.visit(self)
    
    # OVERRIDE
    def __str__(self):
        return self.rawMeasurement + ' : ' + self.timeStamp

    def getAttributesDictionary(self):
        return {
            self.__class__.__name__ : (self.rawMeasurement, self.timeStamp), 
            }

class ReadingContainer(models.Model):
    # readings = model.ManytoMany(Reading, on_delete=models.CASCADE)
    pass