# Generated by Django 5.1.6 on 2025-02-27 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=50, unique=True)),
                ('country', models.CharField(default='Lietuva', max_length=100)),
                ('coordination_x', models.FloatField(default=0)),
                ('coordination_y', models.FloatField(default=0)),
            ],
        ),
    ]
