from django.shortcuts import redirect, render
from django.http import HttpResponse, Http404
from .models import Movie


def index(request):
    """ Creates an HTTP response for requests made to the index route. """

    if request.method == 'POST':
        Movie.objects.create(title=request.POST['movie_title'])
        return redirect('/movies/')

    movies = Movie.objects.all()

    return render(request, 'movies/index.html', {'movie_list': movies})

## Commenting this view out until we decide as a group to reimplement separate lists

# def view_list(request):

#     movies = Movie.objects.all()

#     return render(request, 'movies/list.html', {'movie_list': movies})
