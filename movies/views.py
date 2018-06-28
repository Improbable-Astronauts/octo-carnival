from django.shortcuts import redirect, render
from django.http import HttpResponse, Http404
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib import messages

import omdb

from .models import Movie


def index(request):
    """ Creates an HTTP response for requests made to the index route. """

    if request.method == 'POST':
        try:
            movie_dict = omdb.imdbid(request.POST['imdb_id'])
            #TODO fix this so that movie_dict is passed directly to Movie.objects.create()
            Movie.objects.create(title=movie_dict['title'],year=movie_dict['year'],
                            imdb_id=movie_dict['imdb_id'],runtime=movie_dict['runtime'],
                            rated=movie_dict['rated'],)
            return redirect('/')
        except MultiValueDictKeyError:
            
            messages.add_message(request, messages.WARNING, 'You didn\'t select a movie to save, look for another?')
            return render(request, 'movies/search.html')
           
            
    movies = Movie.objects.all()

    return render(request, 'movies/index.html', {'movie_list': movies})


def search(request):
    if request.method == 'POST':
        returned_values = omdb.search_movie(request.POST['movie_title'])
        return render(request, 'movies/search.html', {'movie_results': returned_values })

    return render(request, 'movies/search.html')


def detail(request):

    return HttpResponse("<h1>Movie Detail View</h1>")
