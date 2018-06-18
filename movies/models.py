from django.db import models


class Movie(models.Model):
    """ Defines the class of Movie objects. """

    title = models.TextField(default='')
    year = models.IntegerField(default=1900)
    imdb_id = models.TextField(default='')
    runtime = models.TextField(default='')
    rated = models.TextField(default='Unknown')

    def __str__(self):
        """ Returns helpful identifiers about a movie object. """
        return self.title

