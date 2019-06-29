# from django.test import TestCase
# from movies.models import Movie


# class HomePageTest(TestCase):

#     def test_uses_index_template(self):

#         response = self.client.get('/')
#         self.assertTemplateUsed(response, 'movies/index.html')

#     def test_can_save_a_POST_request(self):

#         response = self.client.post('/', data={'imdb_id': 'tt0092099'})
#         self.assertEqual(Movie.objects.count(), 1)
#         new_movie = Movie.objects.first()
#         self.assertEqual(new_movie.title, 'Top Gun')

#     def test_redirects_after_POST(self):

#         response = self.client.post('/', data={'imdb_id': 'tt0092099'})
#         self.assertEqual(response.status_code, 302)
#         self.assertEqual(response['location'], '/')

#     def test_displays_all_movies(self):

#         Movie.objects.create(title='Galaxy Quest',imdb_id='tt0177789')
#         Movie.objects.create(title='Clue',imdb_id='tt0088930')

#         response = self.client.get('/')

#         self.assertContains(response, 'Galaxy Quest')
#         self.assertContains(response, 'Clue')

#     def test_only_saves_movies_when_necessary(self):

#         self.client.get('/')
#         self.assertEqual(Movie.objects.count(), 0)


# class SearchPageTest(TestCase):

#     def test_uses_search_template(self):
#         response = self.client.get('/search/')
#         self.assertTemplateUsed(response, 'movies/search.html')


#     def test_displays_all_search_results(self):
#         response = self.client.post('/search/', {'movie_title':'clue'})
#         self.assertContains(response, 'Clue')
#         self.assertContains(response, 'Without a Clue')
#         self.assertContains(response, 'Get a Clue')
#         self.assertContains(response, 'No Clue')


#     def test_displays_no_results_message_as_needed(self):
#         response = self.client.post('/search/', {'movie_title':'Awesome Adam Sandler Movie'})
#         self.assertContains(response, "No results found. ")


#     def test_redirects_to_movie_detail_view(self):

#         pass  # add after api calls are working


# class MovieModelTest(TestCase):

#     def test_saving_and_retrieving_items(self):

#         first_movie = Movie()
#         first_movie.title = 'The first (ever) movie title'
#         first_movie.save()

#         second_movie = Movie()
#         second_movie.title = 'A sequel'
#         second_movie.save()

#         saved_movies = Movie.objects.all()
#         self.assertEqual(saved_movies.count(), 2)

#         first_saved_movie = saved_movies[0]
#         second_saved_movie = saved_movies[1]
#         self.assertEqual(first_saved_movie.title, 'The first (ever) movie title')
#         self.assertEqual(second_saved_movie.title, 'A sequel')
