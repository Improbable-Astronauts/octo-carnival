from django.test import TestCase
from movies.models import Movie


class HomePageTest(TestCase):

    def test_uses_index_template(self):

        response = self.client.get('/movies/')
        self.assertTemplateUsed(response, 'movies/index.html')

    def test_can_save_a_POST_request(self):

        response = self.client.post('/movies/', data={'movie_title': 'A Movie Title'})
        self.assertEqual(Movie.objects.count(), 1)
        new_movie = Movie.objects.first()
        self.assertEqual(new_movie.title, 'A Movie Title')

    def test_redirects_after_POST(self):

        response = self.client.post('/movies/', data={'movie_title': 'A Movie Title'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/movies/')

    def test_displays_all_movies(self):

        Movie.objects.create(title='Galaxy Quest')
        Movie.objects.create(title='Clue')

        response = self.client.get('/movies/')

        self.assertContains(response, 'Galaxy Quest')
        self.assertContains(response, 'Clue')

    def test_only_saves_movies_when_necessary(self):

        self.client.get('/movies/')
        self.assertEqual(Movie.objects.count(), 0)


class MovieModelTest(TestCase):

    def test_saving_and_retrieving_items(self):

        first_movie = Movie()
        first_movie.title = 'The first (ever) movie title'
        first_movie.save()

        second_movie = Movie()
        second_movie.title = 'A sequel'
        second_movie.save()

        saved_movies = Movie.objects.all()
        self.assertEqual(saved_movies.count(), 2)

        first_saved_movie = saved_movies[0]
        second_saved_movie = saved_movies[1]
        self.assertEqual(first_saved_movie.title, 'The first (ever) movie title')
        self.assertEqual(second_saved_movie.title, 'A sequel')

## Commenting these out until we start using multiple lists in our projects

# class ListViewTest(TestCase):

#     def test_displays_all_movies(self):

#         Movie.objects.create(title='Galaxy Quest')
#         Movie.objects.create(title='Clue')

#         response = self.client.get('/movies/lists/the-only-list-in-the-world/')

#         self.assertContains(response, 'Galaxy Quest')
#         self.assertContains(response, 'Clue')

#     def test_uses_list_template(self):

#         response = self.client.get('/movies/lists/the-only-list-in-the-world/')

#         self.assertTemplateUsed(response, 'movies/list.html')
