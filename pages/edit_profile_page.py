from selenium.webdriver.common.by import By

from pages.abstract.weather_page import WeatherPage
from pages.home_page import MainPage


class EditProfilePage(WeatherPage):

    locator_dictionary = WeatherPage.locator_dictionary
    locator_dictionary.update({
        "my_profile_form": (By.CSS_SELECTOR, '#manageForm'),
        "first_name_input": (By.CSS_SELECTOR, '#firstName'),
        "username_input": (By.CSS_SELECTOR, '#username'),
        "birthdate_input": (By.CSS_SELECTOR, '#birthdate'),
        "birthdate_valid": (By.CSS_SELECTOR, 'div[data-birthdate-input] div.form-control-wrapper.form-control-valid'),
        "save_form_button": (By.CSS_SELECTOR, '#manageForm  button[type=submit]'),
        "form_saved_successful_popup": (By.CSS_SELECTOR, '#toastr-container .toastr-success'),
        "delete_account_link": (By.CSS_SELECTOR, '#manageForm a.text-danger.pull-right'),
    })

    def __wait_for_form(self):
        self.wait_for_visibility_of_element(self.find_element(self.locator_dictionary["my_profile_form"]))

    def fill_user_form(self, user):
        self.__wait_for_form()

        self.find_element(self.locator_dictionary["first_name_input"]).send_keys(user.first_name)
        self.find_element(self.locator_dictionary["username_input"]).send_keys(user.username)
        self.find_element(self.locator_dictionary["birthdate_input"]).send_keys(user.birthdate)

        self.wait_for_presence_of_element(self.locator_dictionary["birthdate_valid"])
        self.find_element(self.locator_dictionary["save_form_button"]).click()

        self.wait_for_presence_of_element(self.locator_dictionary["form_saved_successful_popup"], 2)
        return self

    def get_first_name_from_form(self):
        return self.find_element(self.locator_dictionary["first_name_input"]).get_attribute("value")

    def get_username_from_form(self):
        return self.find_element(self.locator_dictionary["username_input"]).get_attribute("value")

    def get_birthdate_from_form(self):
        return self.find_element(self.locator_dictionary["birthdate_input"]).get_attribute("value")

    def delete_account(self):
        self.__wait_for_form()

        self.find_element(self.locator_dictionary["delete_account_link"]).click()
        self.wait_for_alert_to_appear()

        self.driver.switch_to.alert.accept()

        self.wait_for_removal_of_element(self.find_element(self.locator_dictionary["my_profile_form"]))

        return MainPage(self.driver)
