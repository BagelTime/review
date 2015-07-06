from django.db import models

class Category(models.Model):
    """"category to rate the movie on"""

    icon = models.FileField(upload_to='icons', max_length=100)
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class CategoryRafting(models.Model):
    """rating for category to rate the movie on"""

    category = models.ForeignKey("Category")
    movie = models.ForeignKey("Movie")
    rating = models.BigIntegerField(choices=((0,0), (1,1), (2,2), (3,3), (4,4), (5,5)))

    def __unicode__(self):
        return "%s %s %s" % (self.movie.title, self.category.name, self.rating)


class Movie(models.Model):
    """The Movie"""

    db_id = models.IntegerField(default=-1)
    title = models.CharField(max_length=200)
    #rating = models.CharField(max_length=10, choices=(('NR', 'NR'), ('G', 'G'), ('PG', 'PG'), ('PG-13', 'PG-13'), ('R', 'R'), ('NC-17', 'NC-17')))
    #summary = models.TextField()
    #review = models.TextField()
    #genre = models.ManyToManyField("Genre")


    def __unicode__(self):
        return self.title


class Genre(models.Model):
   """"General Category of Movie"""
   # icon = models.ImageField(upload_to='icons', max_length=100)
   name = models.CharField(max_length=100)


   def __unicode__(self):
       return self.name
