# Generated by Django 4.0.2 on 2022-09-02 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='builder',
            name='description',
        ),
        migrations.AddField(
            model_name='scheam',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
