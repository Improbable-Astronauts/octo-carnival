from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, Http404


import omdb

from .models import Movie


def index(request):
    """ Creates an HTTP response for requests made to the index route. """

    if request.method == 'POST':
        movie_dict = omdb.imdbid(request.POST['imdb_id'])
        #TODO fix this so that movie_dict is passed directly to Movie.objects.create()
        Movie.objects.create(title=movie_dict['title'],year=movie_dict['year'],
                        imdb_id=movie_dict['imdb_id'],runtime=movie_dict['runtime'],
                        rated=movie_dict['rated'],)
        return redirect('/')
    movies = Movie.objects.all()

    return render(request, 'movies/index.html', {'movie_list': movies})


def search(request):
    if request.method == 'POST':
        returned_values = omdb.search_movie(request.POST['movie_title'])
        return render(request, 'movies/search.html', {'movie_results': returned_values })

    return render(request, 'movies/search.html')


def detail(request, imdb_id):
    #TODO make imdb_id unique no duplicates in db, hence no multipleObjectReturnedError
    movie = get_object_or_404(Movie, imdb_id=imdb_id)
    
    return render(request, 'movies/detail.html', {'movie':movie})
