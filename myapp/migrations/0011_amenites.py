# Generated by Django 4.0.2 on 2022-09-09 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_builder_address_builder_city_builder_profileimg_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amenites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AirConditioning', models.BooleanField(default=False)),
                ('CleaningService', models.BooleanField(default=False)),
                ('Lift', models.BooleanField(default=False)),
                ('Dishwasher', models.BooleanField(default=False)),
                ('HardwoodFlows', models.BooleanField(default=False)),
                ('SwimmingPool', models.BooleanField(default=False)),
                ('Security', models.BooleanField(default=False)),
                ('ReservedParking', models.BooleanField(default=False)),
                ('OutdoorShower', models.BooleanField(default=False)),
                ('Microwave', models.BooleanField(default=False)),
                ('PetFriendly', models.BooleanField(default=False)),
                ('BasketballCourt', models.BooleanField(default=False)),
                ('Refrigerator', models.BooleanField(default=False)),
                ('Gym', models.BooleanField(default=False)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.scheam')),
            ],
        ),
    ]
