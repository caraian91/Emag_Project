from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    # Atributs
    TOTAL_PRICE_BIG = (By.XPATH, '(//span[@class="emg-right vendor-summary-total-price"]/span)[1]')
    TOTAL_PRICE_SMALL = (By.XPATH, '//span[@class="emg-right vendor-summary-total-price"]//sup')
    DELETE_LINK = (By.XPATH, '//a[contains(text(), "Sterge")]')
    EMPTY_CART_MSG = (By.XPATH, '//div[text()="Cosul tau este gol"]')
    CHECKOUT_BTN = (By.XPATH, '(//a[@href="/cart/checkout"])[1]')

    # Methods
    def verify_total_price(self, expected_price):
        big_price = self.driver.find_element(*self.TOTAL_PRICE_BIG).text
        small_price = self.driver.find_element(*self.TOTAL_PRICE_SMALL).text
        actual_price = big_price + small_price
        self.assertEqual(actual_price, expected_price, "Price is incorrect")

    def click_sterge_link(self):
        self.wait_and_click_elem_by_selector(*self.DELETE_LINK)

    def verify_empty_cart_msg(self):
        self.verify_element_is_displayed_by_selector(*self.EMPTY_CART_MSG)

    def click_checkout_btn(self):
        self.wait_and_click_elem_by_selector(*self.CHECKOUT_BTN)










