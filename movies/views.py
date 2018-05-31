from django.shortcuts import redirect, render
from django.http import HttpResponse, Http404

import omdb

from .models import Movie


def index(request):
    """ Creates an HTTP response for requests made to the index route. """

    if request.method == 'POST':
        Movie.objects.create(title=request.POST['movie_title'])
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
