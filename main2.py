from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import  ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(5)
link ="https://helion.pl/ksiazki/python-wprowadzenie-wydanie-v-mark-lutz,pyth5v.htm"
driver.get(link)

content = driver.find_element(By.ID, "content")
section = content.find_element(By.TAG_NAME, "section")
div= section.find_element(By.TAG_NAME, "div")
book_details = div.find_element(By.CLASS_NAME, 'book-details')
cover_col  = book_details.find_element(By.CLASS_NAME, 'cover-col')
elements_p = cover_col.find_elements(By.TAG_NAME, "p")
element_p = elements_p[-1]
element_a = element_p.find_elements(By.TAG_NAME, 'a')[1]
link = element_a.get_attribute("href")
# zajrzyj

