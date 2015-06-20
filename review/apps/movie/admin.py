from django.contrib import admin
from review.apps.movie.models import Genre, Category, CategoryRafting, Movie

admin.site.register(Genre)
admin.site.register(Category)
admin.site.register(CategoryRafting)
admin.site.register(Movie)
