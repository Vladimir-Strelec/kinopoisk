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

    # def get(self, request, **kwargs):
    #     movie = Movie.objects.get(pk=self.kwargs['pk'])
    #     directors = Actor.objects.filter(film_director__actors__movie=self.kwargs['pk'])
    #     actors = Actor.objects.filter(movie__actors__movie=self.kwargs['pk'])
    #     rating_star = RatingStar.objects.filter(rating__movie_id=self.kwargs['pk'])
    #     return render(request, "movies/moviesingle.html", {'movie': movie})


class SideBarView(ListView):
    model = Movie
    queryset = Movie.objects.all()[:5]
    template_name = "include/side-bar.html"
