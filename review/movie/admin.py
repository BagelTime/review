from django.contrib import admin
from review.movie.models import  Category, CategoryRafting, Movie

#admin.site.register(Genre)
admin.site.register(Category)
admin.site.register(CategoryRafting)
admin.site.register(Movie)