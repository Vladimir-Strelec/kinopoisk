from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from kinopoisk.movies.models import *


class MoviesView(ListView):
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = "movies/movies.html"


class MovieDetailView(DetailView):
    model = Movie
    template_name = "movies/moviesingle.html"

    def get_context_data(self, **kwargs):
        rating_value = [RatingStar.objects.get(id=v['star_id']).value for v in Rating.objects.prefetch_related().filter(movie_id=self.kwargs['pk']).values()]
        context = {
            'movie_shots': MovieShots.objects.filter(movie_id=kwargs['object'].pk),
            'movie': Movie.objects.get(pk=self.kwargs['pk']),
            'movie_side_bar': Movie.objects.all()[0:5:-1],
            'rating_star': sum(rating_value) / len(rating_value),
        }
        return context

