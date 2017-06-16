from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.abstract.weather_page import WeatherPage
from pages.home_page import MainPage


class EditProfilePage(WeatherPage):

    locator_dictionary = WeatherPage.locator_dictionary
    locator_dictionary.update({
        "my_profile_form": (By.CSS_SELECTOR, '#manageProfileForm[novalidate=true]'),
        "first_name_input": (By.CSS_SELECTOR, 'input[name=firstName]'),
        "username_input": (By.CSS_SELECTOR, 'input[name=userName]'),
        "birthdate_month_select": (By.CSS_SELECTOR, '.birthdate-dropdown > div:nth-of-type(1) select'),
        "birthdate_day_select": (By.CSS_SELECTOR, '.birthdate-dropdown > div:nth-of-type(2) select'),
        "birthdate_year_select": (By.CSS_SELECTOR, '.birthdate-dropdown > div:nth-of-type(3) select'),
        "save_form_button": (By.CSS_SELECTOR, '#manageProfileForm  button[type=submit]'),
        "form_saved_successful_indicator": (By.CSS_SELECTOR, '#manageProfileForm button[type=submit].btn-disabled'),
        "delete_account_link": (By.CSS_SELECTOR, '#manageProfileForm + div.profile-delete-button'),
    })

    def __wait_for_form(self):
        self.wait_for_presence_of_element(self.locator_dictionary["my_profile_form"])

    def fill_user_form(self, user):
        self.__wait_for_form()

        self.find_element(self.locator_dictionary["first_name_input"]).send_keys(user.first_name)
        self.find_element(self.locator_dictionary["username_input"]).send_keys(user.username)

        month, day, year = user.birthdate.split(" / ")

        Select(self.find_element(self.locator_dictionary["birthdate_month_select"])).select_by_value(month)
        Select(self.find_element(self.locator_dictionary["birthdate_day_select"])).select_by_value(day)
        Select(self.find_element(self.locator_dictionary["birthdate_year_select"])).select_by_value(year)

        self.find_element(self.locator_dictionary["save_form_button"]).click()

        self.wait_for_presence_of_element(self.locator_dictionary["form_saved_successful_indicator"], 2)
        return self

    def get_first_name_from_form(self):
        return self.find_element(self.locator_dictionary["first_name_input"]).get_attribute("value")

    def get_username_from_form(self):
        return self.find_element(self.locator_dictionary["username_input"]).get_attribute("value")

    def get_birthdate_from_form(self):
        month = Select(self.find_element(self.locator_dictionary["birthdate_month_select"])).first_selected_option.get_attribute("value")
        day = Select(self.find_element(self.locator_dictionary["birthdate_day_select"])).first_selected_option.get_attribute("value")
        year = Select(self.find_element(self.locator_dictionary["birthdate_year_select"])).first_selected_option.get_attribute("value")
        return " / ".join([month, day, year])

    def delete_account(self, user):
        self.__wait_for_form()

        self.find_element(self.locator_dictionary["delete_account_link"]).click()
        self.wait_for_alert_to_appear()

        self.driver.switch_to.alert.accept()

        self.wait_for_removal_of_element(self.find_element(self.locator_dictionary["my_profile_form"]))
        user.delete_file()

        return MainPage(self.driver)
