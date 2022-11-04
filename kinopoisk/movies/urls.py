from django.urls import path

from kinopoisk.movies.views import *

urlpatterns = (
    path("", MoviesView.as_view(), name="movies"),
    path("details/<int:pk>/", MovieDetailView.as_view(), name="movie_details"),
)
