from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys

from pages.abstract.weather_page import WeatherPage
from pages.account_quickstart_page import AccountQuickstartPage


class CreateAccountPage(WeatherPage):
    '''
    Apparently, Sign Up form is not fully functional when Selenium thinks that page
    is loaded (probably due to async JS). We have to wait until unspecified event
    finishes. One of visible changes in process is setting up value 'novalidate'
    attribute of <form> element, which we use as wait inidicator.
    '''
    locator_dictionary = WeatherPage.locator_dictionary
    locator_dictionary.update({
        "loaded_form_indicator": (By.CSS_SELECTOR, '#loginSignUpForm[novalidate=true]'),
        "email_input": (By.CSS_SELECTOR, 'input[name=id]'),
        "password_input": (By.CSS_SELECTOR, 'input[name=token]'),
        "toc_checkbox_label": (By.CSS_SELECTOR, '.signup-agreement .checkbox span'),
        "signup_button": (By.CSS_SELECTOR, '#loginSignUpForm button[type=submit]')
    })

    def fill_create_account_form(self, user):
        self.wait_for_presence_of_element(self.locator_dictionary["loaded_form_indicator"])
        self.find_element(self.locator_dictionary["email_input"]).send_keys(user.email)
        self.find_element(self.locator_dictionary["password_input"]).send_keys(user.password)
        if user.accept_toc:
            self.find_element(self.locator_dictionary["toc_checkbox_label"]).click()
        self.find_element(self.locator_dictionary["signup_button"]).click()
        return AccountQuickstartPage(self.driver)
