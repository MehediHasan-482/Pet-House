# Generated by Django 5.1.2 on 2024-11-29 19:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0002_adopter_pet_adoptionapplication'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnimalDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('health_status', models.CharField(help_text='General health condition of the pet', max_length=100)),
                ('vaccination_status', models.TextField(help_text='Details of completed vaccinations')),
                ('microchipped', models.BooleanField(default=False, help_text='Indicates if the pet is microchipped')),
                ('spayed_neutered', models.BooleanField(default=False, help_text='Indicates if the pet is spayed or neutered')),
                ('special_needs', models.TextField(blank=True, help_text='Details of any special care requirements', null=True)),
                ('animal', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='animal.animal')),
            ],
        ),
    ]
