from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 30

    def find_element(self, locator):
        strategy, location = locator
        return self.driver.find_element(strategy, location)

    def find_elements(self, locator):
        strategy, location = locator
        return self.driver.find_elements(strategy, location)

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def get_page_source(self):
        return self.driver.page_source

    def hover_by_location(self, locator):
        element = self.find_element(locator)
        self.hover(element)

    def hover(self, element):
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def check_element_exists(self, locator):
        try:
            self.find_element(locator)
        except NoSuchElementException:
            return False
        return True

    def wait_for_presence_of_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))

    def wait_for_visibility_of_element(self, element, time=10):
        WebDriverWait(self.driver, time).until(EC.visibility_of(element))

    def wait_for_removal_of_element(self, element, time=10):
        WebDriverWait(self.driver, time).until(EC.staleness_of(element))

    def wait_for_element_to_be_clickable(self, locator, time=10):
        WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator))

    def wait_for_text_in_element(self, locator, text, time=10):
        WebDriverWait(self.driver, time).until(EC.text_to_be_present_in_element(locator, text))