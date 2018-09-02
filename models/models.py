import uuid

from django.db.models import IntegerField, DateTimeField, UUIDField, PositiveSmallIntegerField, Model, \
    PositiveIntegerField, ManyToManyField, TextField, ForeignKey, CASCADE, CharField
from django.core.validators import MaxValueValidator, MinValueValidator


class Command(Model):
    id = UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
        null=False
    )

    code = PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(2**10-1),
            MinValueValidator(0)
        ],
        blank=False,
        null=False
    )

    description = TextField()

    def __str__(self):
        return f'{self.code}'


class I2CSensor(Model):
    id = UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
        null=False,
    )
    address = PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(2**10-1),
            MinValueValidator(0)
        ],
        blank=False
    )
    startUpTime = PositiveIntegerField(
        blank=False,
        default=0
    )
    commands = ManyToManyField(Command)
    # bus = Channel()

    # NamedI2CSensor(I2CSensor):
    # name = CharField(max_length=30)
    # reference = models.CharField(max_length = 30)
    # type = models.CharField(max_length = 30)
    # shortDescription = models.CharField(max_length = 254)

    # OVERRIDE
    def __str__(self):
        return f'{self.address}'


class Reading(Model):
    id = UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
        null=False
    )

    time_stamp = DateTimeField(
        auto_now_add=True,
        editable=False
    )

    raw_measurement = IntegerField(
        editable=False
    )

    sensor = ForeignKey(
        I2CSensor,
        on_delete=CASCADE
    )

    def accept(self, visitor):
        visitor.visit(self)

    # OVERRIDE
    def __str__(self):
        return f'{self.raw_measurement} : {self.time_stamp}'

    def get_attributes_dictionary(self):
        return {
            self.__class__.__name__ : (self.id, self.time_stamp, self.raw_measurement)
        }