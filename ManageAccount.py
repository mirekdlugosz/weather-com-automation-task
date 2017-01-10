import unittest

from configuration import webDriver
from configuration.User import User
from pages.home_page import MainPage
from pages.login_page import LoginPage


class TestPages(unittest.TestCase):
    def setUp(self):
        driver = webDriver.WebDriver()
        self.driver = driver.get_driver()

    def test_login_to_application(self):
        new_user = User().new(True)

        home_page = MainPage(self.driver)

        home_page = home_page.open_register_form()\
            .fill_create_account_form(new_user)\
            .quick_setup_account(new_user)

        self.assertTrue(home_page.user_is_logged_in())

        home_page.logout()

        self.assertFalse(home_page.user_is_logged_in())

    def test_edit_account(self):
        user = User().from_file()

    def test_delete_account(self):
        user = User().from_file()

        home_page = MainPage(self.driver)

        profile_page = home_page.open_login_form().login(user).open_edit_profile()
        profile_page.delete_account()

        login_page = profile_page.open_main_page().open_login_form().login(user)

        self.assertIsInstance(login_page, LoginPage)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
