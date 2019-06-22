from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Actor(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=100)
    year = models.PositiveIntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2020)])
    cast = models.ManyToManyField(Actor, blank=True)
    genres = models.ManyToManyField(Genre, blank=True)
    runtime = models.IntegerField(blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1, blank=False)
    cover_url = models.CharField(max_length=200, blank=True)
    plot_outline = models.TextField(blank=True)
    directors = models.ManyToManyField(Director, blank=True)
    watched = models.BooleanField(default=False)
    favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.name
