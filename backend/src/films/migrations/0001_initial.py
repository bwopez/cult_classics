# Generated by Django 2.2.2 on 2019-06-22 21:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('year', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2020)])),
                ('runtime', models.IntegerField()),
                ('rating', models.DecimalField(decimal_places=1, max_digits=3)),
                ('cover_url', models.CharField(max_length=200)),
                ('plot_outline', models.TextField()),
                ('watched', models.BooleanField(default=False)),
                ('favorite', models.BooleanField(default=False)),
                ('cast', models.ManyToManyField(to='films.Actor')),
                ('directors', models.ManyToManyField(to='films.Director')),
                ('genres', models.ManyToManyField(to='films.Genre')),
            ],
        ),
    ]
