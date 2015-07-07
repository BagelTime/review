from django.db import models
from django.db.models import Avg



class Movie(models.Model):
    """The Movie"""

    db_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)


    def averages(self):
        return self.review_set.aggregate(
             Avg('scare'),
             Avg('gore'),
             Avg('violence'),
             Avg('bad_language'),
             Avg('alcohol_drug'),
             Avg('funny'),
             Avg('sad'),
             Avg('intelectual'),
             Avg('confusing'),
             Avg('romance'),
             Avg('action'),
             Avg('adventure'),
             Avg('kid_friendly'),
             Avg('sexual'),
             Avg('overall'),
             Avg('acting'),
         )


    def __unicode__(self):
        return self.title


class Genre(models.Model):
   """"General Category of Movie"""
   # icon = models.ImageField(upload_to='icons', max_length=100)
   name = models.CharField(max_length=100)


   def __unicode__(self):
       return self.name

class Review(models.Model):
    CHOICES = ((0,'0'), (1,'1'), (2,'2'), (3,'3'), (4,'4'), (5,'5'), (6,'6'), (7,'7'), (8,'8'), (9,'9'), (10,'10'))

    movie = models. ForeignKey(Movie) #parent movie
    review = models.TextField(blank=True, null=True) # text paragraph

    # categories
    scare = models.IntegerField(choices=CHOICES, blank=True, null=True)
    gore = models.IntegerField(choices=CHOICES, blank=True, null=True)
    violence = models.IntegerField(choices=CHOICES, blank=True, null=True)
    bad_language = models.IntegerField(choices=CHOICES, blank=True, null=True)
    alcohol_drug = models.IntegerField(choices=CHOICES, blank=True, null=True)
    funny = models.IntegerField(choices=CHOICES, blank=True, null=True)
    sad = models.IntegerField(choices=CHOICES, blank=True, null=True)
    intelectual = models.IntegerField(choices=CHOICES, blank=True, null=True)
    confusing = models.IntegerField(choices=CHOICES, blank=True, null=True)
    romance = models.IntegerField(choices=CHOICES, blank=True, null=True)
    action = models.IntegerField(choices=CHOICES, blank=True, null=True)
    adventure = models.IntegerField(choices=CHOICES, blank=True, null=True)
    kid_friendly = models.IntegerField(choices=CHOICES, blank=True, null=True)
    sexual = models.IntegerField(choices=CHOICES, blank=True, null=True)
    overall = models.IntegerField(choices=CHOICES, blank=True, null=True)
    acting = models.IntegerField(choices=CHOICES, blank=True, null=True)



    def __unicode__(self):
        return 'Review for %s' % self.movie.title
