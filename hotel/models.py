from django.db.models import *

class Hotel(Model):

    name = CharField(
        'Name of the hotel',
        max_length=64
    )

    address = CharField(
        'Address of the hotel',
        max_length=256
    )

    city = CharField(
        'City',
        max_length=64
    )

    country = CharField(
        'Country',
        max_length=128
    )

    rating = DecimalField(
        'Rating of the hotel',
        decimal_places = 1,
        max_digits = 7
    )

    image = ImageField(
        'Image of the hotel',
        upload_to='hotel-images/%Y/%m/%d'
    )

    description = TextField(
        'Description'
    )

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'Hotel'
        verbose_name_plural = 'Hotels'