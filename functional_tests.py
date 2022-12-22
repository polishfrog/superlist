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

        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertTrue(
            any(row.text == '1: Kupić pawie pióra' for row in rows),
            "Nowy element nie znajduje się w tabeli."
        )

        self.fail('Zakończenie testu')



if __name__ == '__main__':
    unittest.main(warnings="ignore")