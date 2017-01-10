import unittest

from configuration import webDriver
from configuration.User import User
from pages.home_page import MainPage


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

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
