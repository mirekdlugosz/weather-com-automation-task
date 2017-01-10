from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By

from pages.abstract.base import BasePage


class WeatherPage(BasePage):

    locator_dictionary = {
        "buttons_panel": (By.CSS_SELECTOR, '.main-nav-desktop'),
        "login_button": (By.CSS_SELECTOR, '.user-item button.user-login'),
        "register_button": (By.CSS_SELECTOR, '.user-item button.user-signup'),
        "profile_button": (By.CSS_SELECTOR, '.user-item.dropdown > a'),
        "edit_profile_link": (By.CSS_SELECTOR, 'a[data-from-str=hdr_myprofile]'),
        "logout_link": (By.CSS_SELECTOR, 'a[data-from-str=hdr_signout]'),
    }

    def open_main_page(self):
        from pages.home_page import MainPage
        self.driver.get("https://weather.com/404")
        return MainPage(self.driver)

    def open_login_form(self):
        from pages.login_page import LoginPage
        self.wait_for_element_to_be_clickable(self.locator_dictionary["login_button"])
        self.find_element(self.locator_dictionary["login_button"]).click()
        return LoginPage(self.driver)

    def open_register_form(self):
        from pages.create_account_page import CreateAccountPage
        self.wait_for_element_to_be_clickable(self.locator_dictionary["register_button"])
        self.find_element(self.locator_dictionary["register_button"]).click()
        return CreateAccountPage(self.driver)

    def open_edit_profile(self):
        from pages.edit_profile_page import EditProfilePage
        profile_button = self.find_element(self.locator_dictionary["profile_button"])
        self.wait_for_visibility_of_element(profile_button)
        self.hover(profile_button)
        self.find_element(self.locator_dictionary["edit_profile_link"]).click()
        return EditProfilePage(self.driver)

    def logout(self):
        from pages.home_page import MainPage
        profile_button = self.find_element(self.locator_dictionary["profile_button"])
        self.wait_for_visibility_of_element(profile_button)
        self.hover(profile_button)
        self.find_element(self.locator_dictionary["logout_link"]).click()
        self.wait_for_removal_of_element(profile_button)
        return MainPage(self.driver)

    def user_is_logged_in(self):
        return self.find_element(self.locator_dictionary["profile_button"]).is_displayed()