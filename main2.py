from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import  ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://helion.pl/search?szukaj=python")
driver.maximize_window()
driver.implicitly_wait(5)
form = driver.find_element(By.CLASS_NAME, 'filter-form')
list_format = form.find_element(By.ID, "filtrFormat").find_elements(By.CLASS_NAME, "checkbox-line")
label_format = list_format[2].find_element(By.TAG_NAME, 'label')
checbox =  list_format[2].find_element(By.TAG_NAME, 'input')
print(checbox.get_attribute("id"))
driver.execute_script("""
    
""")

# driver.execute_script("document.getElementById('scope-playlist-modify-public').click()")