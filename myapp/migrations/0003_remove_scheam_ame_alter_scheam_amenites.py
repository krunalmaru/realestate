# Generated by Django 4.0.2 on 2022-10-13 12:12

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_scheam_ame'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scheam',
            name='ame',
        ),
        migrations.AlterField(
            model_name='scheam',
            name='amenites',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Lift', 'LIFT'), ('Security', 'SECURITY'), ('Garden', 'GARDEN'), ('Reserv Parking', 'RESERVPARKING'), ('Swimming Pull', 'SWIMMINGPULL'), ('Gym', 'GYM'), ('PowerBackup', 'POWERBACKUP')], default=[], max_length=65, null=True),
        ),
    ]
