from django.db import models


class Movie(models.Model):
    """ Defines the class of Movie objects. """

    title = models.TextField(default='')

    def __str__(self):
        """ Returns helpful identifiers about a movie object. """
        return self.title

