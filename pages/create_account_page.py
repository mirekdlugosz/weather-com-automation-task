from selenium.webdriver.common.by import By

from pages.abstract.weather_page import WeatherPage
from pages.account_quickstart_page import AccountQuickstartPage


class CreateAccountPage(WeatherPage):

    locator_dictionary = WeatherPage.locator_dictionary
    locator_dictionary.update({
        "register_form_iframe": (By.CSS_SELECTOR, '.twc-modal-dialog-ups-body iframe'),
        "email_input": (By.CSS_SELECTOR, '#email'),
        "password_input": (By.CSS_SELECTOR, '#password'),
        "toc_checkbox_label": (By.CSS_SELECTOR, 'label[for=cbxAgree]'),
        "signup_button": (By.CSS_SELECTOR, '#signupForm button[type=submit]')
    })

    def fill_create_account_form(self, user):
        self.wait_for_presence_of_element(self.locator_dictionary["register_form_iframe"])

        self.driver.switch_to.frame(self.find_element(self.locator_dictionary["register_form_iframe"]))
        self.wait_for_presence_of_element(self.locator_dictionary["email_input"])
        self.find_element(self.locator_dictionary["email_input"]).send_keys(user.email)
        self.find_element(self.locator_dictionary["password_input"]).send_keys(user.password)
        if user.accept_toc:
            self.find_element(self.locator_dictionary["toc_checkbox_label"]).click()
        self.find_element(self.locator_dictionary["signup_button"]).click()
        return AccountQuickstartPage(self.driver)
