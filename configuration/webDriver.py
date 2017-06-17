# -*- coding: utf-8 -*-

from selenium import webdriver


class WebDriver():
    driver = None

    @classmethod
    def get_driver(self):
        if not self.driver:
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.get("https://weather.com/404")
        return self.driver

    @classmethod
    def close_driver(self):
        self.driver.quit()
        self.driver = None
