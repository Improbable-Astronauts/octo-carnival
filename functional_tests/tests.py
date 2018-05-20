from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        """ Defines setup operations for the NewVisitorTest class. """

        self.browser = webdriver.Firefox()

    def tearDown(self):
        """ Defines tear-down operations for the NewVisitorTest class. """

        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        movies_list = self.browser.find_element_by_id('id_movies_list')
        rows = movies_list.find_elements_by_tag_name('li')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_movies_list_and_retrieve_it_later(self):

        # Jesse has heard about a movie watch-list app, and goes
        # to check out it's homepage

        self.browser.get(self.live_server_url + "/movies/")

        # The page title and header mention to-do movies

        self.assertIn("Movies", self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Movies', header_text)

        # Jesse is immediately invited to enter a movie title

        inputbox = self.browser.find_element_by_id('id_movie_title')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Type a movie title here and press ENTER')

        # Jesse types "John Wick" into a text box (because it's an awesome movie.)

        inputbox.send_keys('John Wick')

        # When they hit enter, the page updates, and now the page lists
        # "1: John Wick" as an item in the "My Favorite Movies list"

        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_for_row_in_list_table('John Wick')

        # There is still a text box inviting Jesse to add another movie.
        # They enter "Constantine" (Jesse may be into Keanu Reeves.)

        inputbox = self.browser.find_element_by_id('id_movie_title')
        inputbox.send_keys('Constantine')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # The page updates again, and now shows both movies on their list.

        movies_list = self.browser.find_element_by_id('id_movies_list')
        rows = movies_list.find_elements_by_tag_name('li')
        self.assertIn('Constantine', [row.text for row in rows])

        # Jesse wonders whether the site will remember their list.  Then
        # they see that the site has generated a unique URL for them --
        # there is some explanatory text to that effect.
        self.fail('Finish the test!')
        # Jesse visits that URL - their movie list is still there.

        # Satisfied, they go back to sleep.
