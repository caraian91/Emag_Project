from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# we define chrome as a browser and maximize windows and open the url
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://emag.ro')

# hover on Laptop, Tablete & Telefoane
laptop = driver.find_element(By.XPATH, '//span[text()="Laptop, Tablete & Telefoane"]')
hover = ActionChains(driver).move_to_element(laptop)
hover.perform()
sleep(2)

# click on Laptopuri
driver.find_element(By.XPATH, '//a[text()="Laptopuri"]').click()
sleep(2)

# add to favorites the laptop
# notice that we start from the product name
# we go up through h2 and div until we have add to favorites contained in the div
# at the end, scroll down to the button that says add to favorites
driver.find_element(By.XPATH, '//a[contains(text(), "ASUS X515MA-EJ450")]/parent::h2/parent::div/parent::div/parent::div//button[@class="add-to-favorites btn"]').click()
sleep(2)

# click on the favorites icon
driver.find_element(By.ID, "my_wishlist").click()
sleep(2)

# I check that i have reached the favorites page url
assert driver.current_url == 'https://www.emag.ro/favorites?ref=ua_favorites'
sleep(2)

# click on the button Add to Basket from Favorites
driver.find_element(By.XPATH,'//span[contains(text(), "ASUS X515MA-EJ450")]/parent::a/parent::h2/parent::div/parent::div/parent::div//button[text()="Adauga in Cos"]').click()
sleep(2)

# click on the delete buton from Favorites
driver.find_element(By.XPATH, '//span[contains(text(), "ASUS X515MA-EJ450")]/parent::a/parent::h2/parent::div/parent::div/parent::div//span[text()="Sterge"]').click()
sleep(2)
