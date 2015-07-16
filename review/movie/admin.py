from django.contrib import admin
from review.movie.models import Movie, Genre, Review

class ReviewAdmin(admin.ModelAdmin):
    save_as= True


admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Review, ReviewAdmin)
