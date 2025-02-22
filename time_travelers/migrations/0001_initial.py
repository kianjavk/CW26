# Generated by Django 4.2 on 2025-01-09 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TimeTraveler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('national_code', models.CharField(max_length=10, unique=True)),
                ('gender', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'time_travelers',
            },
        ),
    ]
