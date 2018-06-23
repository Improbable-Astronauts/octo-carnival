from django.shortcuts import redirect, render
from django.http import HttpResponse, Http404

import omdb

from .models import Movie
from .imdb_gen import propagate_db

def index(request):
    """ Creates an HTTP response for requests made to the index route. """

    if request.method == 'POST':
        movie_dict = omdb.imdbid(request.POST['imdb_id'])
        #TODO fix this so that movie_dict is passed directly to Movie.objects.create()
        new_movie = Movie.objects.create(title=movie_dict['title'],year=movie_dict['year'],
                        imdb_id=movie_dict['imdb_id'],runtime=movie_dict['runtime'],
                        rated=movie_dict['rated'],)
        
        print("$$$$$$$$$$$$$$$$$$" + new_movie.title)
        new_movie.save()
        print("SAVED")
        return redirect('/')
    movies = Movie.objects.all()

    return render(request, 'movies/index.html', {'movie_list': movies})


def search(request):
    if request.method == 'POST':
        returned_values = omdb.search_movie(request.POST['movie_title'])
        return render(request, 'movies/search.html', {'movie_results': returned_values })

    return render(request, 'movies/search.html')


def detail(request):

    return HttpResponse("<h1>Movie Detail View</h1>")

def propagate(request):
    if request.method == 'POST':
        instances = request.POST['number_of_movies']

        print("%%%%%%%%%" + instances)
        propagate_db(int(instances))
        movies = Movie.objects.all()
        return render(request, 'movies/index.html', {'movie_list':movies})
    return render(request, 'movies/propagate.html')