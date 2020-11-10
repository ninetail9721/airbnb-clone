from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    list_filter = UserAdmin.list_filter + (
        "preference",
        "language",
        "fav_book_genre",
        "fav_movie_genre",
    )

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "bio",
                    "preference",
                    "language",
                    "fav_book_genre",
                    "fav_movie_genre",
                ),
            },
        ),
    )