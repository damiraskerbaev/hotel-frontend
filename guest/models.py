from django.db.models import *
from django.core.validators import MinLengthValidator, MaxLengthValidator

class Guest(Model):
    first_name = CharField(
        'First name',
        max_length=64
    )

    last_name = CharField(
        'Last name',
        max_length=64
    )

    email = EmailField(
        'Email'
    )

    phone_number = CharField(
        'Phone number',
        max_length=13
    )

    passport_serie = IntegerField(
        'Passport serie'
    )

    def __str__(self):
        return f'{self.first_name}'
    
    class Meta:
        verbose_name='Guest'
        verbose_name_plural='Guests'