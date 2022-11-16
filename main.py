from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest

class MainTests(unittest.TestCase):
    def test_demo_login(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.helion.pl")
        title = driver.title
        assert "Księgarnia internetowa informatyczna Helion.pl - wydawnictwo informatyczne, książki, kursy" == title
        driver.quit()
    def test_search(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.helion.pl")
        driver.implicitly_wait(5)
        previous_title = driver.title
        search = driver.find_element(By.ID, 'inputSearch')
        search.click()
        # search.send_keys("python")
        search.send_keys(Keys.ENTER)
        sleep(6)
        title = driver.title
        assert previous_title == title
        driver.quit()
    def test_search_word(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.helion.pl")
        driver.implicitly_wait(5)
        previous_title = driver.title
        search = driver.find_element(By.ID, 'inputSearch')
        search.click()
        search.send_keys("python")
        search.send_keys(Keys.ENTER)
        sleep(6)
        title = driver.title
        assert previous_title == title
        driver.quit()
# driver.close()