# Generated by Django 4.0.2 on 2022-09-07 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheam',
            name='rooms',
            field=models.IntegerField(default=''),
        ),
        
    ]
