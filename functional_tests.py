from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        """ Defines setup operations for the NewVisitorTest class. """

        self.browser = webdriver.Firefox()

    def tearDown(self):
        """ Defines tear-down operations for the NewVisitorTest class. """

        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

        # Jesse has heard about a movie watch-list app, and goes
        # to check out it's homepage

        self.browser.get('http://localhost:8000/movies/')

        # The page title and header mention to-do movies
        self.assertIn("Movies", self.browser.title)
        self.fail('Finish the test!')

        # Jesse is immediately invited to enter a movie title

        # Jesse types "John Wick" into a text box (because it's an awesome movie.)

        # When they hit enter, the page updates, and now the page lists
        # "1: John Wick" as an item in the "My Favorite Movies list"

        # There is still a text box inviting Jesse to add another movie.
        # They enter "Constantine" (Jesse may be into Keanu Reeves.)

        # The page updates again, and now shows both movies on their list.

        # Jesse wonders whether the site will remember their list.  Then
        # they see that the site has generated a unique URL for them --
        # there is some explanatory text to that effect.

        # Jesse visits that URL - their movie list is still there.

        # Satisfied, they go back to sleep.

if __name__ == "__main__":
    unittest.main(warnings='ignore')