from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.helion.pl")
driver.implicitly_wait(5)
search = driver.find_element(By.ID, 'inputSearch')
search.click()
# search.send_keys("python")
search.send_keys(Keys.ENTER)
sleep(6)
driver.close()