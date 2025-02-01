# Generated by Django 5.1.2 on 2024-12-01 09:13

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_member_donate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('u_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('availability', models.CharField(help_text='e.g., Weekends, Weekdays, Flexible', max_length=100)),
                ('skills', models.TextField(help_text='Describe your skills or experience relevant to volunteering.')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
