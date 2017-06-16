# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from pages.abstract.weather_page import WeatherPage
from pages.home_page import MainPage


class ManageLocationsPage(WeatherPage):

    locator_dictionary = WeatherPage.locator_dictionary
    locator_dictionary.update({
        "home_address_input": (By.CSS_SELECTOR, '.container-fluid.hidden-xs .address-typeahead input'),
        "address_autocomplete_item": (By.CSS_SELECTOR, '.container-fluid.hidden-xs .address-typeahead .results li p'),
        "location_nickname_input": (By.CSS_SELECTOR, '.container-fluid.hidden-xs input[data-ng-model="newLocationHandler.nickname"]'),
        "save_button": (By.CSS_SELECTOR, '.container-fluid.hidden-xs button.btn-primary'),
        "saved_locations_item": (By.CSS_SELECTOR, 'ul.saved-list li .location-row'),
    })

    def add_location(self, user):
        self.wait_for_presence_of_element(self.locator_dictionary["home_address_input"])
        self.find_element(self.locator_dictionary["home_address_input"]).send_keys(user.city)

        try:
            self.wait_for_presence_of_element(self.locator_dictionary["address_autocomplete_item"])
        except TimeoutException:
            print("DEBUG: Could not find any location for {}".format(user.city))
            return False
        self.find_element(self.locator_dictionary["address_autocomplete_item"]).click()

        self.find_element(self.locator_dictionary["location_nickname_input"]).send_keys(user.city)

        self.find_element(self.locator_dictionary["save_button"]).click()

        self.wait_for_presence_of_element(self.locator_dictionary["saved_locations_item"])

        self.open_main_page()

        return MainPage(self.driver)
