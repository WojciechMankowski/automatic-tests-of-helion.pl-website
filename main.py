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
        search = driver.find_element(By.ID, 'inputSearch')
        search.click()
        search.send_keys("python")
        sleep(10)
        element = driver.find_element(By.CSS_SELECTOR, 'li.wszystkie')
        button = element.find_element(By.CSS_SELECTOR, "p.button").find_element(By.TAG_NAME, "a")
        driver.get(button.get_attribute('href'))
        assert driver.title == '"python" - Wyniki wyszukiwania - Wydawnictwo Helion, księgarnia helion.pl'
    def test_select_categpry(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://helion.pl/search?szukaj=python")
        driver.implicitly_wait(5)
        panle_category = driver.find_element(By.CLASS_NAME, 'sub-categories')
        list_elements = panle_category.find_elements(By.TAG_NAME, "li")
        selected_item = list_elements[1].find_element(By.TAG_NAME, "h4").find_element(By.TAG_NAME, "a")
        driver.get(selected_item.get_attribute("href"))
        panle_category = driver.find_element(By.CLASS_NAME, 'sub-categories')
        list_elements = panle_category.find_elements(By.TAG_NAME, "li")
        selected_item = list_elements[0].find_element(By.TAG_NAME, "h4").find_element(By.TAG_NAME, "a")
        assert selected_item.get_attribute('title') == ".NET - Programowanie"
    def test_seleced_format(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://helion.pl/search?szukaj=python")
        driver.implicitly_wait(5)
        panle_category = driver.find_element(By.CLASS_NAME, 'sub-categories')
        list_elements = panle_category.find_elements(By.TAG_NAME, "li")
        selected_item = list_elements[1].find_element(By.TAG_NAME, "h4").find_element(By.TAG_NAME, "a")
        driver.get(selected_item.get_attribute("href"))
        panle_category = driver.find_element(By.CLASS_NAME, 'sub-categories')
        list_elements = panle_category.find_elements(By.TAG_NAME, "li")
        selected_item = list_elements[0].find_element(By.TAG_NAME, "h4").find_element(By.TAG_NAME, "a")
        driver.get(selected_item.get_attribute('href'))
        print(driver.current_url)
        assert driver.current_url == 'https://helion.pl/search/?szukaj=python&wsprzed=1&formaty=p&ceny=-'
# driver.close()