from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductsPage(BasePage):

    RESULTS_TITLE = (By.XPATH, '//a[@data-zone="title"]')
    VEZI_DETALII_COS_BTN = (By.XPATH, '//a[text()="Vezi detalii cos"]')
    PRODUSE_FAVORITE_BTN = (By.ID, "my_wishlist")

    def click_vezi_detalii_cos(self):
        self.wait_and_click_elem_by_selector(*self.VEZI_DETALII_COS_BTN)

    def verify_results_contain_text(self, text):
        title_list = self.driver.find_elements(*self.RESULTS_TITLE)
        for i in range(5):
            title = title_list[i].text.lower()
            self.assertTrue(text in title, 'Result does not contain search query')

    def add_to_basket_by_partial_product_name(self, partial_name):
        self.driver.find_element(By.XPATH, f'//a[contains(text(), "{partial_name}")]/parent::h2/parent::div/parent::div/parent::div//button[text()="Adauga in Cos"]').click()

    # New change 13.01.2023
    def add_to_favorites_by_partial_product_name(self, name):
        self.driver.find_element(By.XPATH, f'//a[contains(text(), "{name}")]/parent::h2/parent::div/parent::div/parent::div//button[@class="add-to-favorites btn"]').click()

    def delete_from_favorites_by_partial_product_name(self, partial_name):
        self.driver.find_element(By.XPATH, f'//span[contains(text(), "{partial_name}")]/parent::a/parent::h2/parent::div/parent::div/parent::div//span[text()="Sterge"]').click()

    def click_produse_favorite(self):
        self.wait_and_click_elem_by_selector(*self.PRODUSE_FAVORITE_BTN)

    def add_to_basket_by_partial_name_but_from_favorites_list(self, partial_name):
        self.driver.find_element(By.XPATH, f'//span[contains(text(), "{partial_name}")]/parent::a/parent::h2/parent::div/parent::div/parent::div//button[text()="Adauga in Cos"]').click()






