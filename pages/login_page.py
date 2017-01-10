from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from pages.abstract.weather_page import WeatherPage
from pages.home_page import MainPage


class LoginPage(WeatherPage):

    locator_dictionary = WeatherPage.locator_dictionary
    locator_dictionary.update({
        "login_form_iframe": (By.CSS_SELECTOR, '.twc-modal-dialog-ups-body iframe'),
        "email_input": (By.CSS_SELECTOR, '#email'),
        "password_input": (By.CSS_SELECTOR, '#password'),
        "log_in_button": (By.CSS_SELECTOR, '#LogInBtn'),
        "invalid_login_popup": (By.CSS_SELECTOR, '#toastr-container .toastr-error')
    })

    def login(self, user):
        self.wait_for_presence_of_element(self.locator_dictionary["login_form_iframe"])

        self.driver.switch_to_frame(self.find_element(self.locator_dictionary["login_form_iframe"]))
        self.wait_for_presence_of_element(self.locator_dictionary["email_input"])
        self.find_element(self.locator_dictionary["email_input"]).send_keys(user.email)
        self.find_element(self.locator_dictionary["password_input"]).send_keys(user.password)
        self.find_element(self.locator_dictionary["log_in_button"]).click()

        try:
            self.wait_for_presence_of_element(self.locator_dictionary["invalid_login_popup"], 2)
            self.driver.switch_to_default_content()
            return self
        except TimeoutException:
            self.driver.switch_to_default_content()
            self.wait_for_visibility_of_element(self.find_element(self.locator_dictionary["profile_button"]))
            return MainPage(self.driver)