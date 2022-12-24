import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('lista', header_text)

        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Wpisz rzeczy do zrobienia'
        )

        inputbox.send_keys('Kupić pawie pióra')
        inputbox.send_keys(Keys.ENTER)


    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element(By.TAG_NAME, 'table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertIn(row_text, [row.text for row in rows])



if __name__ == '__main__':
    unittest.main(warnings="ignore")