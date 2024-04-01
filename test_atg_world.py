import unittest
from selenium import webdriver

class TestWebsiteLoading(unittest.TestCase):
    def setUp(self):
        # Open a browser window
        self.driver = webdriver.Chrome()

    def test_website_loading(self):
        # Open the website
        self.driver.get("https://atg.world")

        # Verify if the website title contains expected text
        self.assertIn("Across The Globe (ATG) - Professional and Personal Social Networking", self.driver.title)

    def tearDown(self):
        # Close the browser window
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
