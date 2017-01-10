from selenium.webdriver.common.by import By

from pages.abstract.weather_page import WeatherPage
from pages.home_page import MainPage


class EditProfilePage(WeatherPage):

    locator_dictionary = WeatherPage.locator_dictionary
    locator_dictionary.update({
        "my_profile_form": (By.CSS_SELECTOR, '#manageForm'),
        "delete_account_link": (By.CSS_SELECTOR, '#manageForm a.text-danger.pull-right')
    })

    def __wait_for_form(self):
        self.wait_for_visibility_of_element(self.find_element(self.locator_dictionary["my_profile_form"]))

    def delete_account(self):
        self.__wait_for_form()

        self.find_element(self.locator_dictionary["delete_account_link"]).click()
        self.wait_for_alert_to_appear()

        self.driver.switch_to_alert().accept()

        self.wait_for_removal_of_element(self.find_element(self.locator_dictionary["my_profile_form"]))

        return MainPage(self.driver)