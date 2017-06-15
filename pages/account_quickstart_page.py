from selenium.webdriver.common.by import By

from pages.abstract.weather_page import WeatherPage
from pages.manage_locations_page import ManageLocationsPage


class AccountQuickstartPage(WeatherPage):

    locator_dictionary = WeatherPage.locator_dictionary
    locator_dictionary.update({
        "manage_locations_link": (By.CSS_SELECTOR, '.page-container .complete-spot + p a'),
    })

    def quick_setup_account(self, user):
        self.wait_for_presence_of_element(self.locator_dictionary["manage_locations_link"])
        self.find_element(self.locator_dictionary["manage_locations_link"]).click()
        return ManageLocationsPage(self.driver)
