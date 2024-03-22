# Generated by Django 4.2.8 on 2024-03-20 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64, verbose_name='First name')),
                ('last_name', models.CharField(max_length=64, verbose_name='Last name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone_number', models.CharField(max_length=13, verbose_name='Phone number')),
                ('passport_serie', models.IntegerField(verbose_name='Passport serie')),
            ],
        ),
    ]
