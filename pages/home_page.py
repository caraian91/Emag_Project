from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from time import sleep


class HomePage(BasePage):
    # Atributs
    ACCEPT_COOKIES_BTN = (By.XPATH, '//button[text()="Accept"]')
    ENTER_YOUR_ACCOUNT_BTN = (By.XPATH, '(//a[@id="my_account"]//i)[1]')
    HELLO_MSG = (By.XPATH, '//p/strong[contains(text(), "Salut")]')
    SEARCH_INPUT = (By.ID, 'searchboxTrigger')
    ENTER_YOUR_ACCOUNT_CLOSE_BTN = (By.XPATH, '(//i[@class="em em-close"])[3]')

    # Methods
    def navigate_to_home_page(self):
        self.driver.get('https://www.emag.ro/')

    def click_accept_cookies_btn(self):
        self.click_if_present_by_selector(*self.ACCEPT_COOKIES_BTN)

    def click_enter_in_account_close_btn(self):
        self.click_if_present_by_selector(*self.ENTER_YOUR_ACCOUNT_CLOSE_BTN )

    def search_after(self, query):
        self.wait_and_fill_elem_by_selector(*self.SEARCH_INPUT, query)

    def click_my_account_btn(self):
        self.wait_and_click_elem_by_selector(*self.ENTER_YOUR_ACCOUNT_BTN)

    def verify_login_message(self, expected_msg):
        self.verify_text_on_elem_by_selector(*self.HELLO_MSG, expected_msg)

    def verify_url_message(self):
        self.verify_page_url('https://www.emag.ro/')

    def hover_over_menu_category(self, category_name):
        category = self.driver.find_element(By.XPATH, f'//span[text()="{category_name}"]')
        self.hover_by_elem(category)

    def click_menu_subcategory(self, subcategory_name):
        self.wait_and_click_elem_by_selector(By.XPATH, f'//a[text()="{subcategory_name}"]')









