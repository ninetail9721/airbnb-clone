from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    PREFERENCE_BOOKS = "books"
    PREFERENCE_MOVIES = "movies"

    PREFERENCE_CHOICES = (
        (PREFERENCE_BOOKS, "Books"),
        (PREFERENCE_MOVIES, "Movies"),
    )

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "kr"

    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, "English"),
        (LANGUAGE_KOREAN, "Korean"),
    )

    ACTION = "action"
    ADVENTURE = "adventure"
    COMEDY = "comedy"
    CRIME = "crime"
    DRAMAFANTASY = "dramafantasy"
    HISTORICAL = "historical"
    HORROR = "horror"
    MYSTERY = "mystery"
    ROMANCE = "romance"
    SOCIAL = "social"
    THRILLER = "thriller"
    SCIENCE_FICTION = "science fiction"

    FAV_GENRE = (
        (ACTION, "Action"),
        (ADVENTURE, "Adventure"),
        (COMEDY, "Comedy"),
        (CRIME, "Crime"),
        (DRAMAFANTASY, "Dramafantasy"),
        (HISTORICAL, "Historical"),
        (HORROR, "Horror"),
        (MYSTERY, "Mystery"),
        (ROMANCE, "Romance"),
        (SOCIAL, "Social"),
        (THRILLER, "Thriller"),
        (SCIENCE_FICTION, "Science Fiction"),
    )

    bio = models.TextField(blank=True)
    preference = models.CharField(choices=PREFERENCE_CHOICES, max_length=6, blank=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2, blank=True)
    fav_book_genre = models.CharField(choices=FAV_GENRE, max_length=15, blank=True)
    fav_movie_genre = models.CharField(choices=FAV_GENRE, max_length=15, blank=True)
