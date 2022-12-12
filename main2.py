from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver = webdriver.Safari()
driver.maximize_window()
driver.implicitly_wait(5)
link ="https://helion.pl/ksiazki/python-wprowadzenie-wydanie-v-mark-lutz,pyth5v.htm"
driver.get(link)

element = driver.find_element(By.LINK_TEXT, 'Dodaj do koszyka')
element.click()
button_plus = driver.find_element(By.CLASS_NAME, 'plus')
print(button_plus.tag_name)
# plus more

# print(element.get_attribute('href'))
# head = element.find_element(By.TAG_NAME, 'h3')
# print(head.text)
