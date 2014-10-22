from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest



class NewVisitorsTest(unittest.TestCase):
	
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)
	
	def tearDown(self):
		self.browser.quit()
	
	def test_can_start_a_list_and_retrieve_it_later(self):
		# Edit has heard about a new online app.  She goes to check out it's
		# home page
		self.browser.get('http://localhost:8000')
		
		# She notices that the title and header mention to-do lists
		self.assertIn('To-Do', self.browser.title)

		# She is invited to enter a todo item right away
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
		)
		
		# She types "Buy peacock feathers" into a text box
		inputbox.send_keys("Buy peacock feathers")
		
		# When she hits enter the page updates and now the page lists:
		# 1: Buy peacock feathers as an item in the todo list
		inputbox.send_keys(keys.ENTER)
		
		table = self.browser.find_element_by_id('id_list_table')
		row = table.find_elements_by_tag_name('tr')
		assertTrue(
			any(row.text == '1: Buy peacock feathers' for row in rows)
		)


		# There is still another text box inviting her to add another item.  She
		# enters "Use peacock feathers to make a fly" 
		self.fail('finish the test')


		# She presses enter and now shows both items on her list

		# Edith wonders if the site will remeber her list.  She sees that the
		# site has created a unique URL for her -- there is some explanation text

		# She visits the URL and the list is there

		# Satisfied she goes to sleep
		
if __name__ == '__main__':
	unittest.main(warnings='ignore')


