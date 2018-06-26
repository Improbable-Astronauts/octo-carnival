from django.urls import path
from . import views

app_name = 'movies' # needed to use namespace in moviemvp urls

urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search, name='search'),
    path('detail', views.detail, name='movie_detail')
]