from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    # Atributs
    EMAIL_INPUT = (By.ID, 'user_login_email')
    PASSWORD_INPUT = (By.ID, 'user_login_password')
    CONTINUE_BTN = (By.ID, 'user_login_continue')
    ACTIVATE_LATER_BTN = (By.XPATH, '//a[text()="Activează mai târziu"]')
    LOGO_IMG = (By.XPATH, '//img[@alt="eMAG"]')

    # Methods
    def set_email(self, email):
        self.wait_and_fill_elem_by_selector(*self.EMAIL_INPUT, email)

    def set_password(self, password):
        self.wait_and_fill_elem_by_selector(*self.PASSWORD_INPUT, password)

    def click_continue_btn(self):
        self.wait_and_click_elem_by_selector(*self.CONTINUE_BTN)

    def click_activate_later_btn(self):
        self.wait_and_click_elem_by_selector(*self.ACTIVATE_LATER_BTN)

    def click_logo_img(self):
        self.wait_and_click_elem_by_selector(*self.LOGO_IMG)

    def verify_login_url(self):
        self.verify_page_url('https://auth.emag.ro/user/login')






