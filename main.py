from time import sleep
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TestWebHelion(TestCase):

    def configuration_for_Chrome(self) -> WebDriver:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.implicitly_wait(5)
        return driver
    def test_demo_login(self):
        driver = self.configuration_for_Chrome()
        driver.get("https://www.helion.pl")
        title = driver.title
        assert "Księgarnia internetowa informatyczna Helion.pl - wydawnictwo informatyczne, książki, kursy" == title
    def test_search(self):
        driver = self.configuration_for_Chrome()
        driver.get("https://www.helion.pl")
        previous_title = driver.title
        search = driver.find_element(By.ID, 'inputSearch')
        search.click()
        search.send_keys(Keys.ENTER)
        sleep(6)
        title = driver.title
        assert previous_title == title
    def test_search_word(self):
        driver = self.configuration_for_Chrome()
        driver.get("https://www.helion.pl")
        search = driver.find_element(By.ID, 'inputSearch')
        search.click()
        search.send_keys("python")
        sleep(10)
        element = driver.find_element(By.CSS_SELECTOR, 'li.wszystkie')
        button = element.find_element(By.CSS_SELECTOR, "p.button").find_element(By.TAG_NAME, "a")
        driver.get(button.get_attribute('href'))
        assert driver.title == '"python" - Wyniki wyszukiwania - Wydawnictwo Helion, księgarnia helion.pl'
    def test_select_categpry(self):
        driver = self.configuration_for_Chrome()
        driver.get("https://helion.pl/search?szukaj=python")
        panle_category = driver.find_element(By.CLASS_NAME, 'sub-categories')
        list_elements = panle_category.find_elements(By.TAG_NAME, "li")
        selected_item = list_elements[1].find_element(By.TAG_NAME, "h4").find_element(By.TAG_NAME, "a")
        driver.get(selected_item.get_attribute("href"))
        panle_category = driver.find_element(By.CLASS_NAME, 'sub-categories')
        list_elements = panle_category.find_elements(By.TAG_NAME, "li")
        selected_item = list_elements[0].find_element(By.TAG_NAME, "h4").find_element(By.TAG_NAME, "a")
        assert selected_item.get_attribute('title') == ".NET - Programowanie"
    def test_seleced_format(self):
        driver = self.configuration_for_Chrome()
        driver.get("https://helion.pl/search?szukaj=python")
        driver.execute_script("""const content = document.querySelector('#content')
        const section = content.querySelector('section')
        const left = section.querySelector('#left-small-col')
        const leftMenuContainer = left.querySelector('.left-menu-container')
        const filtrFormat= leftMenuContainer.querySelector('#filtrFormat')
        const checkboxLine = filtrFormat.querySelectorAll(".checkbox-line")[2]
        const pdf = checkboxLine.querySelector('input')
        pdf.checked = true""")
        assert driver.current_url == 'https://helion.pl/search/?szukaj=python&wsprzed=1&formaty=p&ceny=-'
    def test_selecd_langues(self):
        driver = self.configuration_for_Chrome()
        driver.get("https://helion.pl/search?szukaj=python")
        form = driver.find_element(By.CLASS_NAME, 'filter-form')
        list_format = form.find_element(By.ID, "filtrJezyk").find_elements(By.CLASS_NAME, "checkbox-line-filters")[1]
        checbox = list_format.find_element(By.TAG_NAME, 'input')
        driver.execute_script("""const content = document.querySelector('#content')
        const section = content.querySelector('section')
        const left = section.querySelector('#left-small-col')
        const leftMenuContainer = left.querySelector('.left-menu-container')
        const filtrFormat= leftMenuContainer.querySelector('#filtrFormat')
        const filtrJezyk = leftMenuContainer.querySelector('#filtrJezyk')

        const languagesFilter = filtrJezyk.querySelector('.languages-filter')
        console.log(languagesFilter)
        const checkboxLlineFilters = document.querySelectorAll('.checkbox-line-filters')[0]
        console.log(checkboxLlineFilters)
        const polish = checkboxLlineFilters.querySelector("input")
        console.log(polish.checked)
        polish.checked = true
        console.log(polish.checked)""")
        list_format = form.find_elements(By.CLASS_NAME, "active")[1]
        labl = list_format.find_element(By.TAG_NAME, 'label').text
        assert labl == "polski"

    def test_select_book(self):
        driver = self.configuration_for_Chrome()
        driver.get('https://helion.pl/search?qa=&szukaj=python&wsprzed=1&formaty=p&ceny=-&jezyk=polski')
        booklistDiv = driver.find_element(By.CLASS_NAME, "book-list-inner")
        ul = booklistDiv.find_element(By.CLASS_NAME, "list")
        list_li = ul.find_elements(By.TAG_NAME, "li")
        link = list_li[0].find_element(By.TAG_NAME, "a").get_attribute("href")
        assert link == "https://helion.pl/ksiazki/python-wprowadzenie-wydanie-v-mark-lutz,pyth5v.htm"

class HelionAbaoutBook(TestCase):
    URL= "https://helion.pl/ksiazki/python-wprowadzenie-wydanie-v-mark-lutz,pyth5v.htm#format/d"
    def configuration_for_Chrome(self) -> WebDriver:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.implicitly_wait(5)
        return driver
    def test_recommendation(self):
        driver = self.configuration_for_Chrome()
        driver.get(self.URL)
        div = driver.find_element(By.CLASS_NAME, "book-description")
        h = div.find_element(By.TAG_NAME, "h3")
        assert h.text == 'Najczęściej kupowane razem'
    def test_bestsellers(self):
        driver = self.configuration_for_Chrome()
        driver.get(self.URL)
        div = driver.find_element(By.CLASS_NAME, "book-description")
        h = div.find_element(By.CLASS_NAME, "similar-products-heading")
        assert h.text == 'Wybrane bestsellery'
    def test_read_pdf(self):
        driver = self.configuration_for_Chrome()
        driver.get(self.URL)
        content = driver.find_element(By.ID, "content")
        section = content.find_element(By.TAG_NAME, "section")
        div = section.find_element(By.TAG_NAME, "div")
        book_details = div.find_element(By.CLASS_NAME, 'book-details')
        cover_col = book_details.find_element(By.CLASS_NAME, 'cover-col')
        elements_p = cover_col.find_elements(By.TAG_NAME, "p")
        element_p = elements_p[-1]
        element_a = element_p.find_elements(By.TAG_NAME, 'a')[1]
        link = element_a.get_attribute("href")
        assert link == 'https://helion.pl/pobierz-fragment/pyth5v/pdf'