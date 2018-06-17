# from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time

MAX_WAIT = 10

class NewVisitorTest(StaticLiveServerTestCase):

    def setUp(self):
        """ Defines setup operations for the NewVisitorTest class. """

        self.browser = webdriver.Firefox()

    def tearDown(self):
        """ Defines tear-down operations for the NewVisitorTest class. """

        self.browser.quit()

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                movies_list = self.browser.find_element_by_id('id_movies_list')
                rows = movies_list.find_elements_by_tag_name('li')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_can_start_a_movies_list_for_one_user(self):

        # Jesse has heard about a movie watch-list app, and goes
        # to check out it's homepage

        self.browser.get(self.live_server_url + "/movies/")
        time.sleep(2)
        #
        # The page title and header mention to-do movies

        self.assertIn("My Movies", self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('movie title', header_text)

        # Jesse is immediately invited to enter a movie title

        inputbox = self.browser.find_element_by_id('id_movie_title')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Submit a movie title')

        # Jesse types "John Wick" into a text box (because it's an awesome movie.)

        inputbox.send_keys('John Wick')

        # When they hit enter, the page updates, and now the page lists
        # "1: John Wick" as an item in the "My Favorite Movies list"

        inputbox.send_keys(Keys.ENTER)

        self.wait_for_row_in_list_table('John Wick')

        # There is still a text box inviting Jesse to add another movie.
        # They enter "Constantine" (Jesse may be into Keanu Reeves.)

        inputbox = self.browser.find_element_by_id('id_movie_title')
        inputbox.send_keys('Constantine')
        inputbox.send_keys(Keys.ENTER)

        # The page updates again, and now shows both movies on their list.

        self.wait_for_row_in_list_table('Constantine')

        # Satisfied, they go back to sleep.
    def test_layout_and_styling(self):
        # Jaques is curious to see the home page
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        # He notices the page is pretty sparse, just adding movies to a list but the form is centerd
        inputbox = self.browser.find_element_by_id('id_movie_title')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512, delta=10
        )
        # He likes the image, it doesn't repeat and takes up the full screen

        # The movies he enters are not bulleted (or bulleted with reels)

