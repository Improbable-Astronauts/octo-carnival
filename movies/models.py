from django.urls import reverse
from django.db import models


class Movie(models.Model):
    """ Defines the class of Movie objects. """

    imdb_id = models.TextField(default='')
    poster = models.TextField(default='')
    runtime = models.TextField(default='')
    rated = models.TextField(default='Unknown')
    title = models.TextField(default='')
    year = models.IntegerField(default=1900)

    def __str__(self):
        """ Returns helpful identifiers about a movie object. """
        return self.title

    def get_absolute_url(self):
        '''returns the correct path to the movie's details'''
        return reverse('movies:detail', args=[self.imdb_id])

