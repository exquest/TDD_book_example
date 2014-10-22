from selenium import webdriver
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
		self.fail('finish the test')

		# She is invited to enter a todo item right away

		# She types "Buy peacock feathers" into a text box

		# When she hits enter the page updates and now the page lists:
		# 1: Buy peacock feathers as an item in the todo list

		# There is still another text box inviting her to add another item.  She
		# enters "Use peacock feathers to make a fly" 

		# She presses enter and now shows both items on her list

		# Edith wonders if the site will remeber her list.  She sees that the
		# site has created a unique URL for her -- there is some explanation text

		# She visits the URL and the list is there

		# Satisfied she goes to sleep
		
if __name__ == '__main__':
	unittest.main(warnings='ignore')


