from datetime import date

from django.db import models


class Category(models.Model):
    name = models.CharField("Category", max_length=150)
    description = models.TextField("Description")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Actor(models.Model):
    name = models.CharField("Name", max_length=100)
    age = models.PositiveSmallIntegerField("Age", default=0)
    description = models.TextField("Description")
    image = models.ImageField("Image", upload_to="actors/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Actors and directors'
        verbose_name_plural = 'Actors and directors'


class Genre(models.Model):
    name = models.CharField("Category", max_length=100)
    description = models.TextField("Description")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'


class Movie(models.Model):
    title = models.CharField("Name", max_length=100)
    tagline = models.CharField("Tagline", max_length=100, default="")
    description = models.TextField("Description")
    poster = models.ImageField('Poster', upload_to="movies/")
    year = models.PositiveSmallIntegerField("The date", default=2019)
    country = models.CharField("Country", max_length=30)
    directors = models.ManyToManyField(Actor, verbose_name="director", related_name="film_director")
    actors = models.ManyToManyField(Actor, verbose_name="actors")
    genres = models.ManyToManyField(Genre, verbose_name="genres")
    world_premiere = models.DateField('Premiere', default=date.today)
    budget = models.PositiveSmallIntegerField('Budget', default=0, help_text='Specify dollar amount')
    fees_in_usa = models.PositiveSmallIntegerField("US fees", default=0, help_text='Specify dollar amount')
    world_in_usa = models.PositiveSmallIntegerField("World fees", default=0, help_text='Specify dollar amount')
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=100, unique=True)
    draft = models.BinaryField("Draft", default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Movi'
        verbose_name_plural = 'Movies'


class MovieShots(models.Model):
    title = models.CharField("Title", max_length=100)
    description = models.TextField("Description")
    image = models.ImageField("Image", upload_to="movie_shots/")
    movie = models.ForeignKey(Movie, verbose_name="Movie", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "film frame"
        verbose_name_plural = "film frames"


class RatingStar(models.Model):
    value = models.SmallIntegerField("Value", default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "rating star"
        verbose_name_plural = "rating stars"


class Rating(models.Model):
    ip = models.CharField("Ip address", max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="star")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="movie")

    def __str__(self):
        return f"{self.star} - {self.movie}"

    class Meta:
        verbose_name = "rating star"
        verbose_name_plural = "rating stars"


class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField("Name", max_length=100)
    text = models.TextField("Text", max_length=5000)
    parent = models.ForeignKey("self", verbose_name="Parent", on_delete=models.SET_NULL, blank=True, null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="movie")

    def __str__(self):
        return f"{self.name} - {self.movie}"

    class Meta:
        verbose_name = "review"
        verbose_name_plural = "reviews"
