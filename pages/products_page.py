from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductsPage(BasePage):
    # Atributs
    RESULTS_TITLE = (By.XPATH, '//a[@data-zone="title"]')
    SEE_CART_DETAILS_BTN = (By.XPATH, '//a[text()="Vezi detalii cos"]')
    FILTER_BRAND_CHECKBOX = (By.XPATH, '(//a[@data-name="Apple"])[1]')
    RESULTS_PRICE = (By.XPATH, '//p[@class="product-new-price"]')

    # Methods
    def click_see_details_cart(self):
        self.wait_and_click_elem_by_selector(*self.SEE_CART_DETAILS_BTN)

    def verify_results_contain_text(self, text):
        title_list = self.driver.find_elements(*self.RESULTS_TITLE)
        for i in range(5):
            title = title_list[i].text.lower()
            self.assertTrue(text in title, 'Result does not contain search query')

    def add_to_basket_product_name(self, name):
        self.wait_scroll_and_click_elem_by_selector(By.XPATH, f'//a[contains(text(), "{name}")]/parent::h2/parent::div/parent::div/parent::div//button[text()="Adauga in Cos"]')

    def filter_by_brand_checkbox(self, brand):
        self.wait_and_click_elem_by_selector(By.XPATH, f'(//a[@data-name="{brand}"])[1]')

    def click_activate_filter_bar_price(self):
        self.wait_and_click_elem_by_selector(By.LINK_TEXT, 'Interval pret')

    def select_interval_price(self, slider_selected, xoffset):
        self.slider_knob(By.XPATH, f'//a[@class="{slider_selected}"]', xoffset)






