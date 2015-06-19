from django.db import models



class Movie(models.Model):
    RATINGS = (
        ('G', 'G'),
        ('PG', 'PG'),
        ('PG-13', 'PG-13'),
        ('R', 'R'),
        ('NC-17', 'NC-17')
    )

    title = models.CharField(max_length=200)
    rating = models.CharField(max_length=10, choices=RATINGS)

    def __unicode__(self):
        return self.title
