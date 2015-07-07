from django.contrib import admin
from review.movie.models import Movie, Genre, Review


admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Review)
