from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By

from pages.abstract.base import BasePage


class WeatherPage(BasePage):

    locator_dictionary = {
        "buttons_panel": (By.CSS_SELECTOR, '.main-nav-desktop'),
        "login_button": (By.CSS_SELECTOR, '.user-item button.user-login'),
        "register_button": (By.CSS_SELECTOR, '.user-item button.user-signup'),
        "profile_button": (By.CSS_SELECTOR, '.main-nav__menulink span.icon-user'),
        "old_profile_button": (By.CSS_SELECTOR, '.user-item.dropdown > a'),
        "edit_profile_link": (By.CSS_SELECTOR, 'a[data-from-str=hdr_myprofile]'),
        "logout_link": (By.CSS_SELECTOR, 'a[data-from-str=hdr_signout]'),
    }

    def __get_profile_element(self):
        for button_name in ("old_profile_button", "profile_button"):
            try:
                profile_button = self.locator_dictionary[button_name]
                self.wait_for_element_to_be_clickable(profile_button, 2)
                return self.find_element(profile_button)
            except (NoSuchElementException, TimeoutException) as e:
                continue
        return None

    def __click_link_on_profile_menu(self, target_locator):
        profile_button = self.__get_profile_element()
        self.hover(profile_button)
        target_button = self.find_element(target_locator)
        self.wait_for_visibility_of_element(target_button)
        target_button.click()
        self.wait_for_removal_of_element(profile_button)

    def open_main_page(self):
        from pages.home_page import MainPage
        self.driver.get("https://weather.com/404")
        return MainPage()

    def open_login_form(self):
        '''
        Yes, this is extremely bad practice. Unfortunately, these links:
        1. Are actually not links, but buttons
        2. That fire JavaScript function on click, which means they don't
           have href attribute or similar, which means we can't obtain targets
        3. Redirect to target pages, except when they randomly decide to
           open target page in new frame.
        It is sad state of affairs when hardcoding URLs is more robust
        than clicking on UI.
        '''
        from pages.login_page import LoginPage
        self.driver.get("https://weather.com/profile/login")
        return LoginPage()

    def open_register_form(self):
        from pages.create_account_page import CreateAccountPage
        self.driver.get("https://weather.com/profile/signup")
        return CreateAccountPage()

    def open_edit_profile(self):
        from pages.edit_profile_page import EditProfilePage
        self.__click_link_on_profile_menu(self.locator_dictionary["edit_profile_link"])
        return EditProfilePage()

    def logout(self):
        from pages.home_page import MainPage
        self.__click_link_on_profile_menu(self.locator_dictionary["logout_link"])
        return MainPage()

    def user_is_logged_in(self):
        profile_button = self.__get_profile_element()
        if not profile_button:
            return False
        return profile_button.is_displayed()
