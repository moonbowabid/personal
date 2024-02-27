import sys
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
    
class TestPersonalBrandWebsite(unittest.TestCase):
    def setUp(self):
        # Set up the WebDriver (in this example, using Chrome)
        self.driver = webdriver.Chrome()
        self.base_url = "https://moonbowabid.github.io/personal/"
        self.driver.get(self.base_url)

    def tearDown(self):
        # Close the browser after each test
        self.driver.quit()

    def test_title(self):
        # Check if the title of the page is correct
        expected_title = "Abid Malik - ECommerce Specialist"
        actual_title = self.driver.title
        self.assertEqual(expected_title, actual_title)

    def test_header_content(self):
        # Check if the header contains the correct name and role
        expected_name = "Abid Malik"
        expected_role = "ECommerce Specialist"

        header = self.driver.find_element(By.CSS_SELECTOR,"header")
        actual_name = header.find_elements(By.TAG_NAME,"h1")[0].text
        actual_role = header.find_elements(By.TAG_NAME,"p")[0].text

        self.assertEqual(expected_name, actual_name)
        self.assertEqual(expected_role, actual_role)

    def test_about_me_content(self):
        # Check if the 'About Me' section has some content
        about_me_section = self.driver.find_element(By.XPATH, "//section[h2='About Me']")
        content = about_me_section.find_elements(By.TAG_NAME,"p")[0].text
        self.assertNotEqual("", content)

    def test_expertise_content(self):
        # Check if the 'Expertise' section has some content
        expertise_section = self.driver.find_element(By.XPATH, "//section[h2='Expertise']")
        content = expertise_section.find_elements(By.TAG_NAME,"p")[0].text
        self.assertNotEqual("", content)

if __name__ == "__main__":
    result = unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestPersonalBrandWebsite))
    sys.exit(not result.wasSuccessful())
    