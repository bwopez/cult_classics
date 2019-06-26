from django import forms
from . import models
import django_filters


class MovieFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")
    genres = django_filters.ModelMultipleChoiceFilter(queryset=models.Genre.objects.all(),
                                                      widget=forms.CheckboxSelectMultiple,
                                                      conjoined=True)
    rating = django_filters.NumberFilter(field_name="rating", lookup_expr="gte")

    class Meta:
        model = models.Movie
        fields = []
