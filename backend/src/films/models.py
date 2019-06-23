from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Genre(models.Model):
    name = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=100)
    year = models.PositiveIntegerField(default=2000, validators=[MinValueValidator(1900), MaxValueValidator(2020)])
    runtime = models.IntegerField(default=1, blank=True, null=True)
    rating = models.DecimalField(default=1.0, max_digits=3, decimal_places=1, blank=True, null=True)
    cover_url = models.CharField(default="Not found", max_length=200, blank=True, null=True)
    plot_outline = models.TextField(default="Not found", blank=True, null=True)
    genres = models.ManyToManyField(Genre, blank=True)
    cast = models.ManyToManyField(Actor, blank=True)
    directors = models.ManyToManyField(Director, blank=True)
    watched = models.BooleanField(default=False)
    favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.name
