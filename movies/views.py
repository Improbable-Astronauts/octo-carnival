from django.shortcuts import redirect, render
from django.http import HttpResponse, Http404
from .models import Movie


def index(request):
    """ Creates an HTTP response for requests made to the index route. """

    if request.method == 'POST':
        Movie.objects.create(title=request.POST['movie_title'])
        return redirect('/movies/lists/the-only-list-in-the-world')

    return render(request, 'movies/index.html')


def view_list(request):

    movies = Movie.objects.all()

    return render(request, 'movies/list.html', {'movie_list': movies})
