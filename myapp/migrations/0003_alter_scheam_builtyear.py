# Generated by Django 4.0.2 on 2022-09-02 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_profile_remove_builder_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheam',
            name='builtyear',
            field=models.DateField(),
        ),
    ]
