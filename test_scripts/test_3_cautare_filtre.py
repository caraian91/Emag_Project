from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep

# navigam la pagina
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://emag.ro')
sleep(2)

# accept cookies
driver.find_element(By.XPATH, '//button[text()="Accept"]').click()
sleep(2)

# inchidem x - intra in cont
driver.find_element(By.XPATH, '(//i[@class="em em-close"])[3]').click()
sleep(2)

# cautam cuvant cheie "laptop"
search = driver.find_element(By.ID, 'searchboxTrigger')
search.send_keys('laptop' + Keys.ENTER)
sleep(2)

# filtram dupa brand "apple"
driver.find_element(By.XPATH, '(//a[@data-name="Apple"])[1]').click()
sleep(2)

# filtram dupa pret activam butonul bar
driver.find_element(By.LINK_TEXT, "Interval pret").click()
sleep(3)

elem1_left = driver.find_element(By.XPATH, "//a[@class='knob left']")
elem2_right = driver.find_element(By.XPATH, "//a[@class='knob right']")
action = ActionChains(driver)
# action.drag_and_drop_by_offset(elem1_left ,20, 0).perform()
# sleep(5)
action.drag_and_drop_by_offset(elem2_right ,-200, 0).perform()
sleep(10)