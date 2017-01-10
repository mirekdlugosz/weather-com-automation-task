# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By

from pages.abstract.weather_page import WeatherPage
from pages.home_page import MainPage


class AccountQuickstartPage(WeatherPage):

    locator_dictionary = WeatherPage.locator_dictionary
    locator_dictionary.update({
        "home_address_input": (By.ID, 'homeLocation'),
        "address_autocomplete_item": (By.CSS_SELECTOR, '#quickstartForm ul.dropdown-menu li'),
        "home_address_valid": (By.CSS_SELECTOR, '#quickstartForm div.form-control-wrapper.form-control-valid'),
        "proceed_button": (By.CSS_SELECTOR, '#quickstartForm button[type=submit]')
    })

    def quick_setup_account(self, user):
        self.wait_for_presence_of_element(self.locator_dictionary["home_address_input"])
        self.find_element(self.locator_dictionary["home_address_input"]).send_keys(user.city)

        self.wait_for_presence_of_element(self.locator_dictionary["address_autocomplete_item"])
        self.find_element(self.locator_dictionary["address_autocomplete_item"]).click()

        self.wait_for_presence_of_element(self.locator_dictionary["home_address_valid"])
        self.find_element(self.locator_dictionary["proceed_button"]).click()

        self.driver.switch_to_default_content()

        self.wait_for_visibility_of_element(self.find_element(self.locator_dictionary["profile_button"]))
        return MainPage(self.driver)