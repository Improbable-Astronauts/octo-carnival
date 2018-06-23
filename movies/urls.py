from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('detail/', views.detail, name='movie_detail'),
    path('propagate/', views.propagate, name='propagate'),
]