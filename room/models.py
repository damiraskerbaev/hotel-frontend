from django.db.models import *
from hotel.models import Hotel

class Room(Model):

    hotel = ForeignKey(
        Hotel,
        verbose_name='Hotel',
        
        on_delete=CASCADE
    )

    number = PositiveSmallIntegerField(
        'Number of the room'
    )

    capacity = PositiveSmallIntegerField(
        'Capacity'
    )

    price_per_night = PositiveBigIntegerField(
        'Price per night ($)'
    )

    is_used = BooleanField(
        'Is used'
    )

    description = TextField(
        'Description'
    )


    def __str__(self):
        return f'{self.number}'
    
    class Meta:
        verbose_name = 'Room'
        verbose_name_plural = 'Rooms'