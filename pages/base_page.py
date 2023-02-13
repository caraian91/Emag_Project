from browser import Browser
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

class BasePage(Browser):
    # Methods
    def wait_for_elem_by_selector(self, by, selector):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((by, selector)))

    def wait_and_click_elem_by_selector(self, by, selector):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((by, selector)))
        self.driver.find_element(by, selector).click()

    def click_if_present_by_selector(self, by, selector):
        elem_list = self.driver.find_elements(by, selector)
        if len(elem_list) == 1:
            self.wait_scroll_and_click_elem_by_selector(by, selector)

    def wait_scroll_and_click_elem_by_selector(self, by, selector):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((by, selector)))
        elem = self.driver.find_element(by, selector)
        self.driver.execute_script("arguments[0].scrollIntoView();", elem)
        self.driver.execute_script("arguments[0].click();", elem)

    def wait_and_fill_elem_by_selector(self, by, selector, text):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((by, selector)))
        self.driver.find_element(by, selector).send_keys(text + Keys.ENTER)

    def verify_element_is_displayed_by_selector(self, by, selector):
        elem = self.driver.find_element(by, selector)
        self.assertTrue(elem.is_displayed(), 'Elem not displayed')

    def verify_text_on_elem_by_selector(self, by, selector, expected_text):
        actual = self.driver.find_element(by, selector).text
        self.assertEqual(expected_text, actual, 'Text on element is incorrect')

    def verify_page_url(self, expected_url):
        actual = self.driver.current_url
        self.assertEqual(expected_url, actual, 'URL is incorrect')

    def hover_by_selector(self, by, selector):
        elem = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((by, selector)))
        hover = ActionChains(self.driver).move_to_element(elem)
        hover.perform()

    def hover_by_elem(self, elem):
        actions = ActionChains(self.driver).move_to_element(elem)
        actions.perform()

    def slider_knob(self, by, selector, xoffset):
        elem = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((by, selector)))
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(elem, xoffset, 0).perform()
