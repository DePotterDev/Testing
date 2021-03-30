from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Check out homepage
        self.browser.get('http://localhost:8000')

        # User notices the page title and header mention to-do
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # User is needs to enter a to-do item
        # User types "Buy cat food" into a text box
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )


        # When user hits enter, the page updates, and now the page lists
        # "1: Buy cat food" as an item in the to-do list        
        inputbox.send_keys(Keys.Enter)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )


        # There is still a text box inviting her to add another item.
        # The user enters "8 pack of coca-cola's"
        self.fail('Finish the test!')

        # The page updates again, and now shows both items on the user's list

        # The user copies the url and paste it again to see if the site remembers
        # The site is still there with it's items.
        


if __name__ == '__main__':
    unittest.main(warnings='ignore')