from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    EMAIL_INPUT = (By.ID, 'user_login_email')
    PASSWORD_INPUT = (By.ID, 'user_login_password')
    CONTINUA_BTN = (By.ID, 'user_login_continue')
    ACTIVEAZA_MAI_TARZIU_BTN = (By.XPATH, '//a[text()="Activează mai târziu"]')
    LOGO_IMG = (By.XPATH, '//img[@alt="eMAG"]')

    def set_email(self, email):
        self.wait_and_fill_elem_by_selector(*self.EMAIL_INPUT, email)

    def set_password(self, email):
        self.wait_and_fill_elem_by_selector(*self.PASSWORD_INPUT, email)

    def click_continua_btn(self):
        self.wait_and_click_elem_by_selector(*self.CONTINUA_BTN)

    def click_activeaza_mai_tarziu_btn(self):
        self.wait_and_click_elem_by_selector(*self.ACTIVEAZA_MAI_TARZIU_BTN)

    def click_logo_img(self):
        self.wait_and_click_elem_by_selector(*self.LOGO_IMG)

    def verify_login_url(self):
        self.verify_page_url('https://auth.emag.ro/user/login')

    def verify_favorites_url(self):
        self.verify_page_url('https://www.emag.ro/favorites?ref=ua_favorites')





