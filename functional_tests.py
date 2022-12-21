from selenium import webdriver
import unittest


class NewVisionTest(unittest.TestCase):

    def setUp(self):
        """Open web"""
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        """End test"""
        self.browser.quit()

    def test_can_start(self):
        """User into to main website"""
        self.browser.get('http://127.0.0.1:8000/')

        self.assertIn('Listy', self.browser.title)
        self.fail('Zakończenie testu')



if __name__ == '__main__':
    unittest.main(warnings="ignore")