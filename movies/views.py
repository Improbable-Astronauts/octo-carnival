from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Movie

def index(request):
    """ Creates an HTTP response for requests made to the index route. """

    all_movies = Movie.objects.all()

    if len(all_movies) > 0:
        context = {'movie_list': all_movies, }

    else:
        context = {}

    return render(request, 'movies/index.html', context)
