from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time

MAX_WAIT = 10

class NewVisitorTest(LiveServerTestCase):

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

        self.wait_for_row_in_list_table('John Wick')

        # There is still a text box inviting Jesse to add another movie.
        # They enter "Constantine" (Jesse may be into Keanu Reeves.)

        inputbox = self.browser.find_element_by_id('id_movie_title')
        inputbox.send_keys('Constantine')
        inputbox.send_keys(Keys.ENTER)

        # The page updates again, and now shows both movies on their list.

        self.wait_for_row_in_list_table('Constantine')

        # Satisfied, they go back to sleep.

    def test_multiple_users_can_start_lists_at_different_urls(self):

        # Jesse starts a new to-do list
        self.browser.get(self.live_server_url + "/movies/")
        inputbox = self.browser.find_element_by_id('id_movie_title')
        inputbox.send_keys('John Wick 2')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('John Wick 2')

        # They see that the site has generated a unique URL--
        jesse_list_url = self.browser.current_url
        self.assertRegex(jesse_list_url, '/movies/lists/.+')

        # Now a new user, Morgan, comes along to the site.

        ## We use a new browser session to make sure that no information
        ## of Jesse's is coming through from cookies, etc.
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Morgan visits the home page.  There is no sign of Jesse's list.
        self.browser.get(self.live_server_url + '/movies/')
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('John Wick', page_text)
        self.assertNotIn('Constantine', page_text)

        # Morgan starts a new list by entering a new movie.  They are less
        # action-oriented than Jesse.

        inputbox = self.browser.find_element_by_id('id_movie_title')
        inputbox.send_keys('Doubt')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('Doubt')

        # Morgan gets their own unique URL
        morgan_list_url = self.browser.current_url
        self.assertRegex(morgan_list_url, '/movies/lists/.+')
        self.assertNotEqual(francis_list_url, jesse_list_url)

        # Again, there is no trace of Jesse's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('John Wick', page_text)
        self.assertIn('Doubt', page_text)
        self.fail('Finish the test!')
